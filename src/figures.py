"""Two figures for the report. Light-mode PNG for the repository README."""
import os, sys, json, itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from agreement import cohen_kappa, gwet_ac, bootstrap_ci
from analyze import load, DIMS, CATS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURFACE   = "#fcfcfb"
INK       = "#0b0b0b"
INK_2     = "#52514e"
MUTED     = "#c9c8c2"
S1, S2    = "#2a78d6", "#eb6834"   # validated adjacent pair, categorical slots 1-2

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "font.size": 10,
    "text.color": INK, "axes.labelcolor": INK_2, "xtick.color": INK_2,
    "ytick.color": INK_2, "axes.edgecolor": MUTED,
    "font.family": "DejaVu Sans",
})

def _clean(ax):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(length=0)
    ax.grid(axis="x", color=MUTED, lw=.6, alpha=.6)
    ax.set_axisbelow(True)


def fig_severity(grades, raters, ids, meta, out):
    """One measure, one axis: mean rubric score. The critical-failure rate is a
    different quantity on a different scale and is reported in the tables and in
    fig_agreement, not rescaled onto this axis."""
    labels = [n.split(" ", 1)[1] for _, n in DIMS]
    fig, ax = plt.subplots(figsize=(8.4, 4.0))
    h = 0.34
    y = np.arange(len(labels))
    for n, (r, col) in enumerate(zip(raters, (S1, S2))):
        vals = [np.mean([grades[r][i][d] for i in ids]) for d, _ in DIMS]
        off = (n - (len(raters) - 1) / 2) * (h + 0.03)
        b = ax.barh(y + off, vals, height=h, color=col,
                    label=f"{r} - {meta[r]['label']}", zorder=3)
        for rect, v in zip(b, vals):
            ax.text(v + .04, rect.get_y() + rect.get_height()/2, f"{v:.2f}",
                    va="center", ha="left", fontsize=9, color=INK_2)
    ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.invert_yaxis(); ax.set_xlim(0, 3.3)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xlabel("Mean rubric score (0 = unacceptable, 3 = strong)")
    ax.set_title("The two judges are not scoring the same system the same way",
                 loc="left", fontsize=12, color=INK, pad=14)
    ax.legend(frameon=False, loc="lower right", fontsize=9)
    _clean(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


def fig_agreement(grades, raters, ids, out):
    a, b = raters[0], raters[1]
    names, kw, lo, hi, ac = [], [], [], [], []
    for d, n in DIMS:
        x = [grades[a][i][d] for i in ids]; y = [grades[b][i][d] for i in ids]
        names.append(n.split(" ", 1)[1])
        kw.append(cohen_kappa(x, y, CATS, "quadratic"))
        c = bootstrap_ci(lambda idx: cohen_kappa([x[j] for j in idx], [y[j] for j in idx],
                                                 CATS, "quadratic"), len(ids))
        lo.append(c[0]); hi.append(c[1])
        ac.append(gwet_ac(x, y, CATS, "quadratic"))
    x = [int(grades[a][i]["critical_failure"]) for i in ids]
    y = [int(grades[b][i]["critical_failure"]) for i in ids]
    names.append("Critical-failure flag")
    kw.append(cohen_kappa(x, y, [0, 1]))
    c = bootstrap_ci(lambda idx: cohen_kappa([x[j] for j in idx], [y[j] for j in idx], [0, 1]), len(ids))
    lo.append(c[0]); hi.append(c[1]); ac.append(gwet_ac(x, y, [0, 1]))

    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    ypos = np.arange(len(names))
    for yy, l, h_ in zip(ypos, lo, hi):
        ax.plot([l, h_], [yy, yy], color=S1, lw=2, alpha=.35, solid_capstyle="round", zorder=2)
    ax.scatter(kw, ypos, s=70, color=S1, zorder=4, label="Cohen's kappa (quadratic weights), with 95% CI")
    ax.scatter(ac, ypos, s=70, color=S2, zorder=4, marker="D", label="Gwet's AC2 / AC1")
    for yy, k, g in zip(ypos, kw, ac):
        ax.text(k, yy - .26, f"{k:.2f}", ha="center", fontsize=9, color=INK_2)
        ax.text(g, yy + .34, f"{g:.2f}", ha="center", fontsize=9, color=INK_2)
    ax.axvline(0, color=MUTED, lw=1, zorder=1)
    ax.set_yticks(ypos); ax.set_yticklabels(names); ax.invert_yaxis()
    ax.set_xlim(-0.15, 1.0); ax.set_xlabel("Agreement coefficient")
    ax.set_ylim(len(names) - 0.35, -0.75)
    ax.set_title("Agreement is low everywhere, and near zero where it matters most",
                 loc="left", fontsize=12, color=INK, pad=34)
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 1.11),
              ncol=2, fontsize=9, handletextpad=.4, columnspacing=1.6)
    _clean(ax)
    fig.tight_layout(); fig.savefig(out, dpi=200); plt.close(fig)


if __name__ == "__main__":
    qs, ans, meta, grades, order = load()
    raters = [r for r in meta if r in grades]
    ids = [i for i in order if all(i in grades[r] for r in raters)]
    os.makedirs(f"{ROOT}/results/figures", exist_ok=True)
    fig_severity(grades, raters, ids, meta, f"{ROOT}/results/figures/rater_severity.png")
    if len(raters) >= 2:
        fig_agreement(grades, raters, ids, f"{ROOT}/results/figures/agreement_by_dimension.png")
    print("figures written")
