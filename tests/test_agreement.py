"""Validation of the agreement estimators against published worked examples."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
from agreement import (cohen_kappa, gwet_ac, fleiss_kappa, krippendorff_alpha,
                       weight_matrix, percent_agreement)

def approx(a, b, tol=1e-3):
    assert abs(a - b) < tol, f"{a} != {b}"

def test_cohen_textbook():
    # 2x2 table [[20,5],[10,15]]: po=.70, pe=.50 -> kappa=.40
    a = [1]*20 + [1]*5 + [0]*10 + [0]*15
    b = [1]*20 + [0]*5 + [1]*10 + [0]*15
    approx(cohen_kappa(a, b, [0, 1]), 0.40)

def test_cohen_matches_sklearn():
    from sklearn.metrics import cohen_kappa_score
    rng = np.random.default_rng(0)
    for scheme, sk in [("identity", None), ("linear", "linear"), ("quadratic", "quadratic")]:
        for _ in range(20):
            a = rng.integers(0, 4, 60).tolist()
            b = [x if rng.random() < .6 else int(rng.integers(0, 4)) for x in a]
            approx(cohen_kappa(a, b, [0,1,2,3], scheme),
                   cohen_kappa_score(a, b, weights=sk, labels=[0,1,2,3]))

def test_perfect_and_independent():
    a = [0,1,2,3]*10
    approx(cohen_kappa(a, a, [0,1,2,3]), 1.0)
    approx(krippendorff_alpha([[x,x] for x in a], "ordinal"), 1.0)
    approx(gwet_ac(a, a, [0,1,2,3]), 1.0)

def test_fleiss_wikipedia():
    # Fleiss (1971) worked example, 10 subjects x 14 raters, 5 categories -> .2099
    counts = [[0,0,0,0,14],[0,2,6,4,2],[0,0,3,5,6],[0,3,9,2,0],[2,2,8,1,1],
              [7,7,0,0,0],[3,2,6,3,0],[2,5,3,2,2],[6,5,2,1,0],[0,2,2,3,7]]
    ratings = []
    for row in counts:
        r = []
        for cat, c in enumerate(row):
            r += [cat]*c
        ratings.append(r)
    approx(fleiss_kappa(ratings, [0,1,2,3,4]), 0.2099, 1e-3)

def test_krippendorff_canonical():
    """Two datasets, both checked against the reference `krippendorff` package.

    Values below were produced by that package and are hard-coded so the test
    runs without it; if the package is installed the test also compares live.
    """
    d1 = [[None,None,None,None,None,3,4,1,2,1,1,3,3,None,3],
          [1,None,2,1,3,3,4,3,None,None,None,None,None,None,None],
          [None,None,2,1,3,4,4,None,2,1,1,3,3,None,4]]
    d2 = [[1,2,3,3,2,1,4,1,2,None,None,None],
          [1,2,3,3,2,2,4,1,2,5,None,3],
          [None,3,3,3,2,3,4,2,2,5,1,None]]
    expected = {
        0: {"nominal": 0.6914, "ordinal": 0.8067, "interval": 0.8108},
        1: {"nominal": 0.6753, "ordinal": 0.8049, "interval": 0.8621},
    }
    for n, d in enumerate((d1, d2)):
        units = list(map(list, zip(*d)))
        for lvl, exp in expected[n].items():
            approx(krippendorff_alpha(units, lvl), exp, 2e-4)
    try:
        import numpy as _np, krippendorff as _kd
    except ImportError:
        return
    for d in (d1, d2):
        rel = [[_np.nan if v is None else v for v in row] for row in d]
        units = list(map(list, zip(*d)))
        for lvl in ("nominal", "ordinal", "interval"):
            approx(krippendorff_alpha(units, lvl),
                   _kd.alpha(reliability_data=rel, level_of_measurement=lvl), 1e-6)

def test_gwet_paradox():
    # Skewed marginals: kappa collapses, AC1 does not. This is why both are
    # reported for the critical-failure flag.
    a = [1]*45 + [1]*4 + [0]*1 + [0]*0
    b = [1]*45 + [0]*4 + [1]*1 + [0]*0
    k = cohen_kappa(a, b, [0,1])
    g = gwet_ac(a, b, [0,1])
    assert k < 0.1 and g > 0.8, (k, g)

def test_weights():
    w = weight_matrix([0,1,2,3], "quadratic")
    approx(w[0,3], 0.0); approx(w[0,0], 1.0); approx(w[0,1], 1 - 1/9)

def test_percent_agreement():
    approx(percent_agreement([0,1,2],[0,1,3]), 2/3)
    approx(percent_agreement([0,1,2],[0,1,3], tolerance=1), 1.0)

if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            try:
                fn(); print("PASS", name)
            except Exception as e:
                fails += 1; print("FAIL", name, e)
    sys.exit(1 if fails else 0)
