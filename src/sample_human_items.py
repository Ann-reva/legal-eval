#!/usr/bin/env python3
"""Select the subset of items for the human rating pass, reproducibly.

Design: one item drawn at random from every (practice-area group x prompt
condition) stratum, so no domain is missing from the human pass, plus enough
high-disagreement items to fill the target size. Both subsets are recorded
separately in the output so the analysis can report them apart - a purposively
chosen high-disagreement item is not evidence about the average item.

    python src/sample_human_items.py --n 15 --seed 2026
"""
from __future__ import annotations
import argparse, json, os, random, sys

sys.path.insert(0, os.path.dirname(__file__))
from analyze import load, DIMS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPS = [("Commercial contracts", "CONTRACT"), ("Corporate", "CORP"), ("Antitrust", "CORP"),
          ("Employment", "EMP"), ("Litigation", "LIT"), ("Privilege", "LIT"),
          ("Data privacy", "PRIV"), ("Health data", "PRIV"), ("AI regulation", "PRIV"),
          ("Securities", "PRIV"), ("Intellectual", "IP"), ("Trade secrets", "IP")]


def group_of(area):
    for prefix, g in GROUPS:
        if area.startswith(prefix):
            return g
    return "MISC"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=15)
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--judges", nargs="*", default=["G2", "G3", "G4"],
                    help="independent judges used to score disagreement")
    a = ap.parse_args()

    qs, ans, meta, grades, order = load()
    J = [j for j in a.judges if j in grades]
    ids = [i for i in order if all(i in grades[j] for j in J)]

    def spread(i):
        s = sum(max(grades[j][i][d] for j in J) - min(grades[j][i][d] for j in J)
                for d, _ in DIMS)
        flags = {grades[j][i]["critical_failure"] for j in J}
        return s + (3 if len(flags) > 1 else 0)

    rng = random.Random(a.seed)
    strata = {}
    for i in ids:
        strata.setdefault((group_of(qs[i]["practice_area"]), ans[i]["gen_condition"]), []).append(i)
    stratified = [rng.choice(sorted(v)) for _, v in sorted(strata.items())]
    rest = [i for i in ids if i not in stratified]
    purposive = sorted(rest, key=lambda i: (-spread(i), i))[:max(0, a.n - len(stratified))]

    out = {"seed": a.seed, "judges": J,
           "stratified": stratified, "high_disagreement": purposive,
           "order": stratified + purposive}
    path = f"{ROOT}/data/_human_sample.json"
    json.dump(out, open(path, "w"), indent=1)
    print(f"{len(strata)} strata -> {len(stratified)} stratified + "
          f"{len(purposive)} high-disagreement = {len(out['order'])} items")
    for n, i in enumerate(out["order"], 1):
        tag = "stratified" if i in stratified else "high-disagreement"
        print(f"{n:2d}. {i:8s} {group_of(qs[i]['practice_area']):9s} "
              f"{ans[i]['gen_condition']:11s} {tag}")


if __name__ == "__main__":
    main()
