"""Produce the agreement report from data/grades/*.jsonl."""
from __future__ import annotations
import json, os, sys, itertools, collections
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from agreement import (cohen_kappa, gwet_ac, fleiss_kappa, krippendorff_alpha,
                       percent_agreement, bootstrap_ci, landis_koch)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIMS = [("D1_accuracy", "D1 Legal accuracy"),
        ("D2_jurisdiction", "D2 Jurisdictional grounding"),
        ("D3_completeness", "D3 Issue completeness"),
        ("D4_authority", "D4 Authority hygiene"),
        ("D5_scope", "D5 Scope discipline")]
CATS = [0, 1, 2, 3]


def load():
    qs = {json.loads(l)["id"]: json.loads(l) for l in open(f"{ROOT}/data/questions.jsonl")}
    ans = {json.loads(l)["id"]: json.loads(l) for l in open(f"{ROOT}/data/answers.jsonl")}
    meta = json.load(open(f"{ROOT}/data/grades/raters.json"))
    grades = {}
    for rid in meta:
        p = f"{ROOT}/data/grades/{rid}.jsonl"
        if not os.path.exists(p):
            continue
        rows = [json.loads(l) for l in open(p) if l.strip()]
        if not rows:
            continue
        grades[rid] = {r["id"]: r for r in rows}
    order = list(qs)
    return qs, ans, meta, grades, order


def fmt(x, nd=3):
    return "n/a" if x != x else f"{x:.{nd}f}"


def main():
    qs, ans, meta, grades, order = load()
    raters = sorted((r for r in meta if r in grades), key=lambda r: r)
    # A rater may cover only part of the set (a human pass usually does). Every
    # statistic below is computed on the items its raters actually share, and the
    # n is reported next to it rather than silently shrinking the whole study.
    cover = {r: [i for i in order if i in grades[r]] for r in raters}
    full = [r for r in raters if len(cover[r]) == len(order)]
    ids = [i for i in order if all(i in grades[r] for r in full)]
    both = lambda a, b: [i for i in order if i in grades[a] and i in grades[b]]
    variants = [r for r in raters if meta[r].get("variant_of")]
    panel = [r for r in raters if r not in variants]
    headline = [r for r in raters if meta[r].get("headline", True) and r not in variants]
    pair = [r for r in raters if meta[r].get("headline_pair")]
    if len(pair) != 2:
        pair = headline[:2] if len(headline) >= 2 else raters[:2]
    excluded = [r for r in raters if r not in headline]
    L = []
    W = L.append

    W("# Inter-rater agreement report\n")
    W(f"Generated from `data/grades/` by `src/analyze.py`. "
      f"{len(ids)} items scored by {len(raters)} rater(s): "
      + ", ".join(f"`{r}` ({meta[r]['label']})" for r in raters) + ".\n")
    if excluded:
        W("> **Excluded from the headline figures:** "
          + ", ".join(f"`{r}`" for r in excluded)
          + ". Their ratings remain in `data/grades/` and in the pairwise tables below, "
            "but every multi-rater statistic is computed over the independent raters only. "
            "The reason is in the panel table.\n")
    if len(pair) == 2:
        W(f"> **Headline pair:** `{pair[0]}` vs `{pair[1]}` - the two independent, "
          "high-capability judges. The disagreement dossier and the concentration "
          "analysis use this pair.\n")

    # ---------------- rater panel ----------------
    W("## 1. Rater panel\n")
    W("| Rater | Model | Items | Execution | Independence |")
    W("|---|---|---|---|---|")
    for r in raters:
        m = meta[r]
        W(f"| `{r}` | {m['model']} | {len(cover[r])}/{len(order)} | {m['execution']} | {m['independence']} |")
    W("")

    # ---------------- leniency ----------------
    W("## 2. Rater severity\n")
    W("Mean score per dimension (0-3) and share of records flagged as a critical failure.\n")
    W("| Rater | " + " | ".join(d[1] for d in DIMS) + " | Critical-failure rate | n |")
    W("|---" * (len(DIMS) + 3) + "|")
    for r in raters:
        cv = cover[r]
        means = [np.mean([grades[r][i][d] for i in cv]) for d, _ in DIMS]
        cf = np.mean([grades[r][i]["critical_failure"] for i in cv])
        W(f"| `{r}` | " + " | ".join(f"{m:.2f}" for m in means)
          + f" | {cf:.0%} | {len(cv)} |")
    W("")
    if len(raters) >= 2:
        cfs = {r: np.mean([grades[r][i]["critical_failure"] for i in cover[r]]) for r in raters}
        d1s = {r: np.mean([grades[r][i]["D1_accuracy"] for i in cover[r]]) for r in raters}
        lo_r, hi_r = min(cfs, key=cfs.get), max(cfs, key=cfs.get)
        W(f"> Across {len(raters)} judges applying the same rubric to the same 40 answers, the "
          f"critical-failure rate runs from **{cfs[lo_r]:.0%}** (`{lo_r}`) to "
          f"**{cfs[hi_r]:.0%}** (`{hi_r}`) - a factor of "
          f"{cfs[hi_r]/max(cfs[lo_r],1e-9):.0f}. Mean legal-accuracy score spans "
          f"{min(d1s.values()):.2f} to {max(d1s.values()):.2f} on a 0-3 scale. The choice of judge, "
          "not the system under test, is the dominant term in what gets reported.\n")

    # ---------------- pairwise ----------------
    W("## 3. Pairwise agreement, by dimension\n")
    W("`kappa` = Cohen's kappa (unweighted). `kappa_w` = quadratically weighted, which is the "
      "appropriate headline for an ordinal scale because it penalises a 3-vs-0 disagreement more "
      "than a 3-vs-2. `AC2` = Gwet's weighted agreement coefficient, reported because kappa is "
      "unstable when one category dominates the marginals. 95% CIs are percentile bootstrap over "
      "items (5,000 resamples).\n")
    pair_rows = []
    for a, b in itertools.combinations(panel, 2):
        pids = both(a, b)
        W(f"### `{a}` vs `{b}`  (n = {len(pids)})\n")
        W("| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |")
        W("|---|---|---|---|---|---|---|---|")
        for d, name in DIMS:
            x = [grades[a][i][d] for i in pids]
            y = [grades[b][i][d] for i in pids]
            kw = cohen_kappa(x, y, CATS, "quadratic")
            ci = bootstrap_ci(lambda idx: cohen_kappa([x[j] for j in idx], [y[j] for j in idx],
                                                      CATS, "quadratic"), len(pids))
            row = dict(dim=name, exact=percent_agreement(x, y), within1=percent_agreement(x, y, 1),
                       k=cohen_kappa(x, y, CATS), kw=kw, ci=ci,
                       ac2=gwet_ac(x, y, CATS, "quadratic"))
            pair_rows.append(((a, b), row))
            W(f"| {name} | {row['exact']:.0%} | {row['within1']:.0%} | {fmt(row['k'])} | "
              f"{fmt(kw)} | [{fmt(ci[0],2)}, {fmt(ci[1],2)}] | {fmt(row['ac2'])} | {landis_koch(kw)} |")
        # critical failure flag
        x = [int(grades[a][i]["critical_failure"]) for i in pids]
        y = [int(grades[b][i]["critical_failure"]) for i in pids]
        k = cohen_kappa(x, y, [0, 1])
        g = gwet_ac(x, y, [0, 1])
        bothf = sum(1 for u, v in zip(x, y) if u and v)
        W(f"| **Critical-failure flag** (binary) | {percent_agreement(x,y):.0%} | - | {fmt(k)} | - | - | {fmt(g)} | {landis_koch(k)} |")
        W("")
        W(f"Confusion on the flag: both raised **{bothf}**, only `{a}` **{sum(x)-bothf}**, "
          f"only `{b}` **{sum(y)-bothf}**, neither **{len(pids)-sum(x)-sum(y)+bothf}**.\n")
    W("")

    # ---------------- multi-rater ----------------
    if len(headline) >= 3:
        W("## 4. Multi-rater agreement\n")
        complete = [r for r in headline if len(cover[r]) == len(order)]
        W("Computed over the independent raters: " + ", ".join(f"`{r}`" for r in headline)
          + ". Krippendorff's alpha uses every rating, including raters who covered only "
            "part of the set - handling missing cells natively is why it is the right "
            "headline statistic here. Fleiss' kappa requires complete cases and is computed "
            "over " + ", ".join(f"`{r}`" for r in complete)
          + f" on all {len(ids)} items.\n")
        W("| Dimension | Fleiss kappa (complete cases) | Krippendorff alpha (ordinal, all ratings) |")
        W("|---|---|---|")
        for d, name in DIMS:
            fl = [[grades[r][i][d] for r in complete] for i in ids]
            kr = [[grades[r][i][d] if i in grades[r] else None for r in headline] for i in order]
            W(f"| {name} | {fmt(fleiss_kappa(fl, CATS))} | {fmt(krippendorff_alpha(kr,'ordinal'))} |")
        fl = [[int(grades[r][i]["critical_failure"]) for r in complete] for i in ids]
        kr = [[int(grades[r][i]["critical_failure"]) if i in grades[r] else None
               for r in headline] for i in order]
        W(f"| **Critical-failure flag** | {fmt(fleiss_kappa(fl,[0,1]))} | "
          f"{fmt(krippendorff_alpha(kr,'nominal'))} |")
        W("")
        W("Per-item spread on the critical-failure flag across the "
          f"{len(complete)} independent judges who scored every item:\n")
        cnt = collections.Counter(sum(int(grades[r][i]["critical_failure"]) for r in complete)
                                  for i in ids)
        W("| Judges flagging the item | Items |")
        W("|---|---|")
        for k2 in range(len(complete) + 1):
            W(f"| {k2} of {len(complete)} | {cnt.get(k2,0)} |")
        W("")
        W(f"> Unanimity - all {len(complete)} agreeing that an item is or is not a "
          f"critical failure - covers **{cnt.get(0,0)+cnt.get(len(complete),0)} of {len(ids)}** items.\n")
    else:
        W("## 4. Multi-rater agreement\n")
        W("Requires three or more raters. Add a third rating pass "
          "(`data/grades/GH.jsonl`, or a cross-vendor judge via `src/run_graders.py`) "
          "and re-run; Fleiss' kappa and Krippendorff's alpha are computed automatically.\n")

    # ---------------- variant arms ----------------
    retest = [r for r in variants if meta[r].get("arm") == "retest"]
    ablate = [r for r in variants if meta[r].get("arm") == "no_gold"]

    if retest:
        W("## 4a. Intra-rater reliability (test-retest)\n")
        W("The same judge, the same prompt, a second independent run in a different "
          "presentation order. This separates two things that a between-rater number "
          "cannot: how much a judge disagrees **with itself** (instrument noise) and how "
          "much judges disagree **with each other** (real, systematic divergence). It "
          "matters here because these models reject the `temperature` parameter, so the "
          "runs could not be pinned to deterministic sampling.\n")
        W("| Judge | " + " | ".join(d[1].split(" ",1)[1] for d in DIMS)
          + " | Critical-failure flag | n |")
        W("|---" * (len(DIMS) + 3) + "|")
        for r in retest:
            base = meta[r]["variant_of"]
            if base not in grades:
                continue
            pids = both(base, r)
            cells = []
            for d, _ in DIMS:
                x = [grades[base][i][d] for i in pids]; y = [grades[r][i][d] for i in pids]
                cells.append(fmt(cohen_kappa(x, y, CATS, "quadratic"), 2))
            x = [int(grades[base][i]["critical_failure"]) for i in pids]
            y = [int(grades[r][i]["critical_failure"]) for i in pids]
            W(f"| `{base}` vs `{r}` | " + " | ".join(cells)
              + f" | {fmt(cohen_kappa(x,y,[0,1]),2)} | {len(pids)} |")
        W("")
        W("> Read this against section 3. Where a judge agrees with **itself** far more "
          "than it agrees with any other judge, the between-rater disagreement does not "
          "look like run-to-run noise. Two bounds on that reading: one repeat bounds the "
          "run-to-run variance without establishing the judge's full behavioural "
          "distribution, and re-running the same prompt says nothing about sensitivity to "
          "how the rubric is worded - the larger risk, and untested here.\n")

    if ablate:
        W("## 4b. Ablation - gold reference withheld\n")
        W("Every judge in section 3 was shown the item's gold reference: the material "
          "points, the trap, and the authorities a practitioner would expect. That makes "
          "part of the task 'match the answer key'. This arm re-runs one judge with the "
          "gold reference removed, so it must rely on its own legal knowledge. The drop "
          "measures how much of the reported agreement the answer key was carrying.\n")
        W("| Comparison | " + " | ".join(d[1].split(" ",1)[1] for d in DIMS)
          + " | Critical-failure flag | n |")
        W("|---" * (len(DIMS) + 3) + "|")
        rows = []
        for r in ablate:
            base = meta[r]["variant_of"]
            rows.append((base, r))
            twin = [t for t in retest if meta[t].get("variant_of") == base]
            for t in twin:
                rows.append((base, t))
        seen = set()
        for base, r in rows:
            if (base, r) in seen or base not in grades:
                continue
            seen.add((base, r))
            pids = both(base, r)
            cells = []
            for d, _ in DIMS:
                x = [grades[base][i][d] for i in pids]; y = [grades[r][i][d] for i in pids]
                cells.append(fmt(cohen_kappa(x, y, CATS, "quadratic"), 2))
            x = [int(grades[base][i]["critical_failure"]) for i in pids]
            y = [int(grades[r][i]["critical_failure"]) for i in pids]
            tag = "same prompt (ceiling)" if meta[r].get("arm") == "retest" else "gold withheld"
            W(f"| `{base}` vs `{r}` - {tag} | " + " | ".join(cells)
              + f" | {fmt(cohen_kappa(x,y,[0,1]),2)} | {len(pids)} |")
        W("")

    # ---------------- construct validity ----------------
    W("## 5. Does the rubric detect the manipulation?\n")
    W("The 40 answers were generated under two prompt conditions: `A_standard` and `B_terse` "
      "(direct, no caveats, under 80 words). If the rubric measures anything real, both judges "
      "should score `B_terse` lower on completeness. This is a construct-validity check on the "
      "rubric, independent of whether the judges agree with each other.\n")
    W("| Rater | Dimension | A_standard | B_terse | Delta |")
    W("|---|---|---|---|---|")
    for r in raters:
        for d, name in DIMS:
            a_ = np.mean([grades[r][i][d] for i in cover[r] if ans[i]["gen_condition"] == "A_standard"])
            b_ = np.mean([grades[r][i][d] for i in cover[r] if ans[i]["gen_condition"] == "B_terse"])
            W(f"| `{r}` | {name} | {a_:.2f} | {b_:.2f} | {b_-a_:+.2f} |")
    W("")

    # ---------------- where the disagreement lives ----------------
    W("## 6. Where the disagreement is concentrated\n")
    if len(pair) == 2:
        a, b = pair
        by_area = collections.defaultdict(list)
        by_diff = collections.defaultdict(list)
        for i in both(a, b):
            gap = np.mean([abs(grades[a][i][d] - grades[b][i][d]) for d, _ in DIMS])
            by_area[qs[i]["practice_area"]].append(gap)
            by_diff[qs[i]["difficulty"]].append(gap)
        W(f"Mean absolute per-dimension gap between `{a}` and `{b}`, by practice area:\n")
        W("| Practice area | n | Mean gap |")
        W("|---|---|---|")
        for k2, v in sorted(by_area.items(), key=lambda kv: -np.mean(kv[1])):
            W(f"| {k2} | {len(v)} | {np.mean(v):.2f} |")
        W("")
        W("By authored difficulty:\n")
        W("| Difficulty | n | Mean gap |")
        W("|---|---|---|")
        for k2, v in sorted(by_diff.items()):
            W(f"| {k2} | {len(v)} | {np.mean(v):.2f} |")
        W("")

    os.makedirs(f"{ROOT}/results", exist_ok=True)
    open(f"{ROOT}/results/agreement_report.md", "w").write("\n".join(L) + "\n")

    # ---------------- long-format CSV ----------------
    import csv
    with open(f"{ROOT}/results/scores_long.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_id", "practice_area", "jurisdiction", "difficulty",
                    "gen_condition", "rater", "dimension", "score"])
        for i in order:
            for r in [r for r in raters if i in grades[r]]:
                for d, _ in DIMS:
                    w.writerow([i, qs[i]["practice_area"], qs[i]["jurisdiction"],
                                qs[i]["difficulty"], ans[i]["gen_condition"], r, d,
                                grades[r][i][d]])
                w.writerow([i, qs[i]["practice_area"], qs[i]["jurisdiction"],
                            qs[i]["difficulty"], ans[i]["gen_condition"], r,
                            "critical_failure", int(grades[r][i]["critical_failure"])])

    # ---------------- disagreement dossier ----------------
    if len(pair) == 2:
        a, b = pair
        D = []
        D.append("# Disagreement dossier\n")
        D.append(f"Every item where `{a}` and `{b}` differ by 2 or more points on any dimension, "
                 "or split on the critical-failure flag. Each entry shows both rationales verbatim, "
                 "so the cause of the split can be read rather than inferred.\n")
        picked = []
        for i in both(a, b):
            gaps = {d: grades[a][i][d] - grades[b][i][d] for d, _ in DIMS}
            flag_split = grades[a][i]["critical_failure"] != grades[b][i]["critical_failure"]
            if max(abs(v) for v in gaps.values()) >= 2 or flag_split:
                picked.append((i, gaps, flag_split))
        D.append(f"**{len(picked)} of {len(both(a,b))} items** qualify.\n")
        for i, gaps, flag_split in picked:
            D.append(f"---\n\n## {i} — {qs[i]['practice_area']} ({qs[i]['jurisdiction']})\n")
            D.append(f"**Question.** {qs[i]['question']}\n")
            D.append(f"**Trap.** {qs[i]['gold']['trap']}\n")
            D.append(f"**Answer under test** (`{ans[i]['gen_condition']}`):\n\n> "
                     + ans[i]["answer"].replace("\n", "\n> ") + "\n")
            D.append("| Dimension | " + f"`{a}`" + " | " + f"`{b}`" + " | Gap |")
            D.append("|---|---|---|---|")
            for d, name in DIMS:
                g = gaps[d]
                mark = " **<-**" if abs(g) >= 2 else ""
                D.append(f"| {name} | {grades[a][i][d]} | {grades[b][i][d]} | {g:+d}{mark} |")
            D.append(f"| Critical failure | {grades[a][i]['critical_failure']} | "
                     f"{grades[b][i]['critical_failure']} | {'**SPLIT**' if flag_split else '-'} |")
            D.append("")
            D.append(f"- `{a}`: {grades[a][i]['rationale']}")
            D.append(f"- `{b}`: {grades[b][i]['rationale']}")
            D.append("")
        open(f"{ROOT}/results/disagreements.md", "w").write("\n".join(D) + "\n")
        print(f"wrote results/disagreements.md ({len(picked)} items)")
    print("wrote results/agreement_report.md, results/scores_long.csv")


if __name__ == "__main__":
    main()
