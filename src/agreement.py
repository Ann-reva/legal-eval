"""Inter-rater agreement statistics, implemented from first principles.

Everything here is deliberately dependency-light (numpy only) so the numbers in
the report can be checked by reading ~200 lines rather than trusting a package.
`tests/test_agreement.py` validates each estimator against published worked
examples.
"""
from __future__ import annotations
import numpy as np

# --------------------------------------------------------------------------- #
# weighting
# --------------------------------------------------------------------------- #

def weight_matrix(categories, scheme="identity"):
    """Agreement weights w[i][j] in [0,1]; 1 = full agreement credit."""
    k = len(categories)
    idx = np.arange(k, dtype=float)
    d = np.abs(idx[:, None] - idx[None, :])
    if scheme == "identity":
        return (d == 0).astype(float)
    if scheme == "linear":
        return 1.0 - d / (k - 1)
    if scheme == "quadratic":
        return 1.0 - (d / (k - 1)) ** 2
    raise ValueError(scheme)


def _confusion(a, b, categories):
    k = len(categories)
    pos = {c: i for i, c in enumerate(categories)}
    m = np.zeros((k, k))
    for x, y in zip(a, b):
        m[pos[x], pos[y]] += 1
    return m


# --------------------------------------------------------------------------- #
# two-rater statistics
# --------------------------------------------------------------------------- #

def cohen_kappa(a, b, categories, scheme="identity"):
    """Cohen's kappa; `scheme` selects unweighted / linear / quadratic weights."""
    a, b = list(a), list(b)
    if not a:
        return float("nan")
    w = weight_matrix(categories, scheme)
    o = _confusion(a, b, categories)
    n = o.sum()
    o = o / n
    r, c = o.sum(axis=1), o.sum(axis=0)
    e = np.outer(r, c)
    po, pe = (w * o).sum(), (w * e).sum()
    if np.isclose(pe, 1.0):
        return float("nan")
    return float((po - pe) / (1 - pe))


def gwet_ac(a, b, categories, scheme="identity"):
    """Gwet's AC1 (identity weights) / AC2 (weighted).

    Uses the same observed agreement as kappa but a chance-agreement term that
    does not collapse when the marginals are skewed - the 'kappa paradox' that
    shows up on any rubric dimension where one category dominates.
    """
    a, b = list(a), list(b)
    if not a:
        return float("nan")
    q = len(categories)
    w = weight_matrix(categories, scheme)
    o = _confusion(a, b, categories)
    o = o / o.sum()
    po = (w * o).sum()
    pi = (o.sum(axis=1) + o.sum(axis=0)) / 2.0
    tw = w.sum()
    pe = (tw / (q * (q - 1))) * float((pi * (1 - pi)).sum())
    if np.isclose(pe, 1.0):
        return float("nan")
    return float((po - pe) / (1 - pe))


def percent_agreement(a, b, tolerance=0):
    a, b = np.asarray(a, float), np.asarray(b, float)
    if a.size == 0:
        return float("nan")
    return float((np.abs(a - b) <= tolerance).mean())


# --------------------------------------------------------------------------- #
# multi-rater statistics
# --------------------------------------------------------------------------- #

def fleiss_kappa(ratings, categories):
    """Fleiss' kappa. `ratings` is a list of per-item lists of category labels.

    Requires the same number of ratings per item (items with fewer are dropped).
    """
    pos = {c: i for i, c in enumerate(categories)}
    counts = []
    n_raters = max(len(r) for r in ratings)
    for r in ratings:
        if len(r) != n_raters:
            continue
        row = [0] * len(categories)
        for v in r:
            row[pos[v]] += 1
        counts.append(row)
    m = np.asarray(counts, float)
    n, k = m.shape
    if n == 0:
        return float("nan")
    p_j = m.sum(axis=0) / (n * n_raters)
    P_i = ((m ** 2).sum(axis=1) - n_raters) / (n_raters * (n_raters - 1))
    po, pe = P_i.mean(), float((p_j ** 2).sum())
    if np.isclose(pe, 1.0):
        return float("nan")
    return float((po - pe) / (1 - pe))


def krippendorff_alpha(units, level="ordinal"):
    """Krippendorff's alpha over a list of per-unit rating lists.

    Handles missing ratings (units rated by only some raters) natively, which is
    why it is the right headline statistic once a human rater scores only a
    subset of the set.
    """
    vals = sorted({v for u in units for v in u if v is not None})
    if len(vals) < 2:
        return float("nan")
    pos = {v: i for i, v in enumerate(vals)}
    k = len(vals)

    coincidence = np.zeros((k, k))
    for u in units:
        u = [v for v in u if v is not None]
        m = len(u)
        if m < 2:
            continue
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                coincidence[pos[u[i]], pos[u[j]]] += 1.0 / (m - 1)

    n_c = coincidence.sum(axis=1)
    n = n_c.sum()
    if n <= 1:
        return float("nan")

    delta = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            if level == "nominal":
                delta[i, j] = 0.0 if i == j else 1.0
            elif level == "interval":
                delta[i, j] = (vals[i] - vals[j]) ** 2
            elif level == "ordinal":
                lo, hi = min(i, j), max(i, j)
                s = n_c[lo:hi + 1].sum() - (n_c[i] + n_c[j]) / 2.0
                delta[i, j] = s ** 2
            else:
                raise ValueError(level)

    d_o = (coincidence * delta).sum() / n
    d_e = (np.outer(n_c, n_c) - np.diag(n_c)).__mul__(delta).sum() / (n * (n - 1))
    if np.isclose(d_e, 0.0):
        return float("nan")
    return float(1 - d_o / d_e)


# --------------------------------------------------------------------------- #
# uncertainty
# --------------------------------------------------------------------------- #

def bootstrap_ci(fn, n_items, n_boot=5000, alpha=0.05, seed=7):
    """Percentile CI by resampling ITEMS (not ratings) with replacement.

    `fn` takes an array of item indices and returns the statistic.
    """
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n_boot):
        idx = rng.integers(0, n_items, n_items)
        v = fn(idx)
        if v == v:  # drop NaN draws (degenerate resamples)
            out.append(v)
    if not out:
        return (float("nan"), float("nan"))
    lo, hi = np.percentile(out, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return float(lo), float(hi)


def landis_koch(k):
    """Conventional verbal label. Reported for orientation only - the bands are
    a rule of thumb from a 1977 paper, not a decision rule."""
    if k != k:
        return "undefined"
    if k < 0.00: return "poor"
    if k < 0.21: return "slight"
    if k < 0.41: return "fair"
    if k < 0.61: return "moderate"
    if k < 0.81: return "substantial"
    return "almost perfect"
