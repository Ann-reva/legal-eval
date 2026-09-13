"""Figures for the report. Light-mode PNG for the repository README.

Palette: categorical slots 1-3 of the reference palette, validated all-pairs in
light mode (worst CVD dE 9.2, worst normal-vision dE 24.0). Slot 3 sits below
3:1 contrast on the light surface, so every bar carries a visible direct label -
the documented relief for that warning.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from agreement import cohen_kappa, gwet_ac, bootstrap_ci
from analyze import load, DIMS, CATS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURFACE, INK, INK_2, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#c9c8c2"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a"]
MODEL_SHORT = {"G2": "Sonnet-class", "G3": "Haiku-class", "G4": "Opus-class",
               "G5": "GPT-class, different vendor"}

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "font.size": 10, "text.color": INK, "axes.labelcolor": INK_2,
    "xtick.color": INK_2, "ytick.color": INK_2, "axes.edgecolor": MUTED,
    "font.family": "DejaVu Sans"})


def _clean(ax, axis="x"):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(length=0)
    ax.grid(axis=axis, color=MUTED, lw=.6, alpha=.6)
    ax.set_axisbelow(True)


def fig_severity(grades, judges, ids, meta, out):
    """Small multiples: one panel per judge, one measure, one hue.

    Past three series a grouped bar chart cannot keep every pair separable for
    colour-vision-deficient readers, so the panel count carries identity here and
    colour carries nothing.
    """
    labels = [n.split(" ", 1)[1] for _, n in DIMS]
    n = len(judges)
    fig, axes = plt.subplots(1, n, figsize=(2.35 * n + 1.6, 3.9), sharex=True)
    if n == 1:
        axes = [axes]
    y = np.arange(len(labels))
    for ax, r in zip(axes, judges):
        cv = [i for i in ids if i in grades[r]] or list(grades[r])
        vals = [np.mean([grades[r][i][d] for i in cv]) for d, _ in DIMS]
        bars = ax.barh(y, vals, height=.55, color=SERIES[0], zorder=3)
        for rect, v in zip(bars, vals):
            ax.text(v + .06, rect.get_y() + rect.get_height() / 2, f"{v:.2f}",
                    va="center", ha="left", fontsize=8, color=INK_2)
        ax.set_title(f"{r} — {meta[r]['label']}\n(n = {len(cv)})",
                     loc="left", fontsize=8.5, color=INK_2, pad=6)
        ax.set_xlim(0, 3.35); ax.set_xticks([0, 1, 2, 3])
        ax.invert_yaxis()
        ax.set_yticks(y)
        ax.set_yticklabels(labels if ax is axes[0] else [])
        _clean(ax)
    fig.suptitle("Mean rubric score by judge (0 = unacceptable, 3 = strong)",
                 x=0.005, ha="left", fontsize=12, color=INK)
    fig.supxlabel("Mean rubric score", fontsize=9, color=INK_2)
    fig.tight_layout(rect=[0, 0.02, 1, 0.94])
    fig.savefig(out, dpi=200); plt.close(fig)


def fig_human_agreement(grades, judges, out):
    """One measure, one axis, one series: how each model judge agrees with the
    human rater on the flag that gates release."""
    rows = []
    for r in judges:
        ids = sorted(set(grades[r]) & set(grades["GH"]))
        if len(ids) < 5:
            continue
        k = cohen_kappa([int(grades[r][i]["critical_failure"]) for i in ids],
                        [int(grades["GH"][i]["critical_failure"]) for i in ids], [0, 1])
        rows.append((r, k, len(ids)))
    rows.sort(key=lambda t: t[1])
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    ypos = np.arange(len(rows))
    bars = ax.barh(ypos, [k for _, k, _ in rows], height=.5, color=SERIES[0], zorder=3)
    for rect, (_, k, _) in zip(bars, rows):
        ax.text(max(k, 0) + .012, rect.get_y() + rect.get_height() / 2, f"{k:.2f}",
                va="center", ha="left", fontsize=9.5, color=INK_2)
    ax.set_yticks(ypos)
    ax.set_yticklabels([f"{r} — {m}" for (r, _, _), m in
                        zip(rows, [MODEL_SHORT.get(r, r) for r, _, _ in rows])])
    ax.set_xlim(0, 0.9); ax.set_xlabel("Cohen's kappa with the human rater (n = 15)")
    ax.set_title("Agreement with the human rater on the critical-failure flag",
                 loc="left", fontsize=12, color=INK, pad=12)
    _clean(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_flag_spread(grades, judges, ids, out):
    """How often the independent judges agree that an item is a critical failure."""
    counts = [sum(int(grades[r][i]["critical_failure"]) for r in judges) for i in ids]
    bars = [counts.count(k) for k in range(len(judges) + 1)]
    fig, ax = plt.subplots(figsize=(8.6, 3.7))
    xs = np.arange(len(bars))
    b = ax.bar(xs, bars, width=.55, color=SERIES[0], zorder=3)
    for rect, v in zip(b, bars):
        ax.text(rect.get_x() + rect.get_width() / 2, v + .35, str(v),
                ha="center", fontsize=10, color=INK_2)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{k} of {len(judges)}" for k in xs])
    ax.set_xlabel("Judges flagging the item as a critical failure")
    ax.set_ylabel("Items")
    ax.set_ylim(0, max(bars) + 3)
    unan = bars[0] + bars[-1]
    ax.set_title(f"The judges agree on only {unan} of {len(ids)} items about what blocks release",
                 loc="left", fontsize=12, color=INK, pad=14)
    _clean(ax, axis="y")
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_agreement(grades, pair, ids, meta, out):
    a, b = pair
    names, kw, lo, hi, ac = [], [], [], [], []
    for d, n in DIMS:
        x = [grades[a][i][d] for i in ids]; y = [grades[b][i][d] for i in ids]
        names.append(n.split(" ", 1)[1])
        kw.append(cohen_kappa(x, y, CATS, "quadratic"))
        c = bootstrap_ci(lambda idx: cohen_kappa([x[j] for j in idx], [y[j] for j in idx],
                                                 CATS, "quadratic"), len(ids))
        lo.append(c[0]); hi.append(c[1]); ac.append(gwet_ac(x, y, CATS, "quadratic"))
    x = [int(grades[a][i]["critical_failure"]) for i in ids]
    y = [int(grades[b][i]["critical_failure"]) for i in ids]
    names.append("Critical-failure flag")
    kw.append(cohen_kappa(x, y, [0, 1]))
    c = bootstrap_ci(lambda idx: cohen_kappa([x[j] for j in idx], [y[j] for j in idx], [0, 1]), len(ids))
    lo.append(c[0]); hi.append(c[1]); ac.append(gwet_ac(x, y, [0, 1]))

    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    ypos = np.arange(len(names))
    for yy, l, h_ in zip(ypos, lo, hi):
        ax.plot([l, h_], [yy, yy], color=SERIES[0], lw=2, alpha=.35,
                solid_capstyle="round", zorder=2)
    ax.scatter(kw, ypos, s=70, color=SERIES[0], zorder=4,
               label="Cohen's kappa (quadratic weights), with 95% CI")
    ax.scatter(ac, ypos, s=70, color=SERIES[1], marker="D", zorder=4, label="Gwet's AC2 / AC1")
    for yy, k, g in zip(ypos, kw, ac):
        ax.text(k, yy - .26, f"{k:.2f}", ha="center", fontsize=9, color=INK_2)
        ax.text(g, yy + .34, f"{g:.2f}", ha="center", fontsize=9, color=INK_2)
    ax.axvline(0, color=MUTED, lw=1, zorder=1)
    ax.set_yticks(ypos); ax.set_yticklabels(names)
    ax.set_ylim(len(names) - 0.35, -0.75)
    ax.set_xlim(-0.15, 1.0); ax.set_xlabel("Agreement coefficient")
    ax.set_title(f"Best case: the two strongest independent judges ({a} vs {b})",
                 loc="left", fontsize=12, color=INK, pad=34)
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 1.11),
              ncol=2, fontsize=9, handletextpad=.4, columnspacing=1.6)
    _clean(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_intra_vs_inter(grades, meta, out):
    """The study's central comparison: a judge against itself, against another
    judge, and against the human rater. Three series, categorical slots 1-3,
    validated all-pairs; every bar carries a direct label."""
    rows = [("G4", "G4b", "Same judge, second run (n=40)"),
            ("G4", "G5", "A judge from a different vendor (n=40)"),
            ("G4", "GH", "The human rater (n=15)")]
    rows = [(a, b, lab) for a, b, lab in rows if a in grades and b in grades]
    labels = [n.split(" ", 1)[1] for _, n in DIMS] + ["Critical-failure flag"]
    fig, ax = plt.subplots(figsize=(8.8, 5.2))
    h = 0.25
    y = np.arange(len(labels))
    for n, ((a, b, lab), col) in enumerate(zip(rows, SERIES)):
        ids = sorted(set(grades[a]) & set(grades[b]))
        vals = []
        for d, _ in DIMS:
            vals.append(cohen_kappa([grades[a][i][d] for i in ids],
                                    [grades[b][i][d] for i in ids], CATS, "quadratic"))
        vals.append(cohen_kappa([int(grades[a][i]["critical_failure"]) for i in ids],
                                [int(grades[b][i]["critical_failure"]) for i in ids], [0, 1]))
        off = (n - (len(rows) - 1) / 2) * (h + 0.03)
        bars = ax.barh(y + off, vals, height=h, color=col, label=lab, zorder=3)
        for rect, v in zip(bars, vals):
            ax.text(max(v, 0) + .015, rect.get_y() + rect.get_height() / 2, f"{v:.2f}",
                    va="center", ha="left", fontsize=8.5, color=INK_2)
    ax.set_yticks(y); ax.set_yticklabels(labels); ax.invert_yaxis()
    ax.set_xlim(0, 1.12); ax.set_xticks([0, .25, .5, .75, 1])
    ax.set_xlabel("Cohen's kappa (quadratic weights; unweighted for the binary flag)")
    ax.set_title("The Opus-class judge against itself, another vendor, and a person",
                 loc="left", fontsize=12, color=INK, pad=38)
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 1.15), ncol=3,
              fontsize=8.5, handletextpad=.4, columnspacing=1.2)
    _clean(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


if __name__ == "__main__":
    qs, ans, meta, grades, order = load()
    raters = sorted(r for r in meta if r in grades)
    complete = [r for r in raters if len([i for i in order if i in grades[r]]) == len(order)]
    ids = [i for i in order if all(i in grades[r] for r in complete)]
    judges = [r for r in raters if meta[r].get("headline", True)
              and not meta[r].get("variant_of") and r in complete]
    pair = [r for r in raters if meta[r].get("headline_pair")] or judges[:2]
    pair = [r for r in pair if r in complete][:2]
    os.makedirs(f"{ROOT}/results/figures", exist_ok=True)
    fig_severity(grades, judges, ids, meta, f"{ROOT}/results/figures/rater_severity.png")
    if "GH" in grades:
        fig_human_agreement(grades, judges, f"{ROOT}/results/figures/human_agreement.png")
    fig_flag_spread(grades, judges, ids, f"{ROOT}/results/figures/critical_failure_spread.png")
    fig_agreement(grades, pair, ids, meta, f"{ROOT}/results/figures/agreement_by_dimension.png")
    fig_intra_vs_inter(grades, meta, f"{ROOT}/results/figures/intra_vs_inter.png")
    print("figures written:", judges, "pair:", pair)
