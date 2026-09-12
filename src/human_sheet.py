#!/usr/bin/env python3
"""Make a human rating sheet, and ingest it back as a rater.

    python src/human_sheet.py --make              # -> results/human_rating_sheet.csv
    # fill the six score columns in a spreadsheet, save as CSV
    python src/human_sheet.py --ingest results/human_rating_sheet.csv --out GH

Partial sheets are fine: rows with blank scores are skipped. Krippendorff's alpha
handles the missing cells, so a human pass over 15 of the 40 items still yields a
usable three-rater figure.
"""
from __future__ import annotations
import argparse, csv, json, os, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIMS = ["D1_accuracy", "D2_jurisdiction", "D3_completeness", "D4_authority", "D5_scope"]


def make(path, seed=99):
    qs = [json.loads(l) for l in open(f"{ROOT}/data/questions.jsonl")]
    ans = {json.loads(l)["id"]: json.loads(l)["answer"] for l in open(f"{ROOT}/data/answers.jsonl")}
    random.Random(seed).shuffle(qs)      # own presentation order; no model scores shown
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "jurisdiction", "question", "must_include", "trap",
                    "authorities", "answer"] + DIMS + ["critical_failure", "rationale"])
        for q in qs:
            w.writerow([q["id"], q["jurisdiction"], q["question"],
                        "\n".join("- " + m for m in q["gold"]["must_include"]),
                        q["gold"]["trap"], "; ".join(q["gold"]["authorities"]),
                        ans[q["id"]]] + [""] * 7)
    print(f"wrote {path} ({len(qs)} rows). Score columns are blank by design - "
          "no model rating is shown, so the human pass stays independent.")


def ingest(path, rater):
    out = []
    with open(path) as f:
        for row in csv.DictReader(f):
            if not all(str(row.get(d, "")).strip() for d in DIMS):
                continue
            rec = {"id": row["id"].strip()}
            for d in DIMS:
                v = int(str(row[d]).strip())
                assert v in (0, 1, 2, 3), f"{rec['id']} {d}={v} out of range"
                rec[d] = v
            cf = str(row.get("critical_failure", "")).strip().lower()
            rec["critical_failure"] = cf in ("1", "true", "yes", "y", "t")
            rec["rationale"] = str(row.get("rationale", "")).strip()
            out.append(rec)
    p = f"{ROOT}/data/grades/{rater}.jsonl"
    with open(p, "w") as f:
        for r in out:
            f.write(json.dumps(r) + "\n")
    mpath = f"{ROOT}/data/grades/raters.json"
    meta = json.load(open(mpath))
    meta.setdefault(rater, {})
    meta[rater].update({"label": "Human rater", "model": "human",
                        "execution": f"manual, {len(out)} of 40 items scored",
                        "independence": "independent; sheet shows no model scores",
                        "role": "human reference"})
    json.dump(meta, open(mpath, "w"), indent=2)
    print(f"wrote {p} ({len(out)} ratings) and registered {rater}. Now: python src/analyze.py")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--make", action="store_true")
    ap.add_argument("--path", default=f"{ROOT}/results/human_rating_sheet.csv")
    ap.add_argument("--ingest")
    ap.add_argument("--out", default="GH")
    a = ap.parse_args()
    if a.make:
        make(a.path)
    elif a.ingest:
        ingest(a.ingest, a.out)
    else:
        ap.error("pass --make or --ingest")
