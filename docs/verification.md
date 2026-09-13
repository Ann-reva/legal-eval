# Verification log

What was checked before the results were written up, and how. Two classes of
error would invalidate this study independently: a wrong statistic, and a wrong
gold reference. Both were checked.

## 1. Statistics

Every estimator in `src/agreement.py` is implemented from scratch and validated
in `tests/test_agreement.py`:

| Estimator | Validated against |
|---|---|
| Cohen's kappa (unweighted) | 2x2 textbook table: po = .70, pe = .50, kappa = .40 |
| Cohen's kappa (unweighted, linear, quadratic) | `sklearn.metrics.cohen_kappa_score`, 60 randomised trials per weighting scheme |
| Fleiss' kappa | Fleiss (1971) worked example, 10 subjects x 14 raters x 5 categories, kappa = 0.2099 |
| Krippendorff's alpha (nominal, ordinal, interval) | the `krippendorff` reference package, on two published datasets with missing cells; agreement to 1e-6 |
| Gwet's AC1 | reduces to the AC2 formula under identity weights; behaviour under skewed marginals asserted directly |
| Weight matrices | quadratic weights checked at the endpoints and one interior cell |
| Percent / adjacent agreement | asserted directly |

Run `python tests/test_agreement.py` — all eight tests pass.

## 2. Legal content

The traps are the part of the item set that carries risk: an item built on a rule
that has changed measures the wrong thing, and a judge that scores against a
stale gold reference produces confidently wrong results. The following were
re-checked against primary or near-primary sources in September 2026.

| Item | Claim checked | Source | Result |
|---|---|---|---|
| PRV-02 | CCPA subdivision letters: "sale" at Civ. Code 1798.140(ad), "share" at (ah) | statute text | confirmed |
| PRV-06 | Item 1.05 runs four business days from the **materiality determination**, not the incident | SEC small-entity compliance guide, quoted verbatim | confirmed |
| CON-06 | Delaware: a reverse triangular merger is not an assignment by operation of law | *Meso Scale Diagnostics v. Roche*, 62 A.3d 62 (Del. Ch. 2013) | confirmed |
| EMP-05 | Cal-WARN: covered establishment at 75 employees, mass layoff at 50 affected in 30 days, 60 days notice | Cal. Lab. Code 1400 et seq. and 2026 practitioner summaries | confirmed, thresholds unchanged |
| ETH-02 | ABA Formal Opinion 512 (July 2024) is the ABA's generative-AI ethics opinion | ABA announcement | confirmed |

**One item to update in the next revision.** California SB 617, effective
1 January 2026, added mandatory content to Cal-WARN notices — Local Workforce
Development Board coordination and contact details, CalFresh information, and a
working employer contact. The EMP-05 gold reference already requires "notice
content and recipients are prescribed", so no score in this run turned on it, but
the authorities list should cite SB 617 when the item set is next revised. Noted
here rather than edited in, because changing a gold reference after grading would
invalidate the ratings that were produced against it.

**Design choice on volatile figures.** Three items — HSR thresholds (COR-06),
FLSA salary level (EMP-01), EU AI Act application dates (PRV-05) — are built on
rules that change on a schedule. Their gold references deliberately do **not**
state a current figure. They require the answer to flag that the figure moves and
to point at the authoritative source. This makes the item set robust to the
passage of time and tests the behaviour that actually matters in a legal product:
knowing which of your facts have expiry dates.

## 3. What was not verified

- The gold references have **not** been reviewed by a licensed attorney. This is
  the single largest gap and no amount of additional rating closes it. See
  limitation **L16** in `METHODOLOGY.md`.
- **Agreement is not accuracy.** The human pass (`GH`, 15 of 40 items) checks
  whether the rubric can be applied consistently against a written gold reference.
  It does not establish which judge is legally right. The rater is a non-expert;
  three of her five dimensions carry almost no variance; and on at least three
  items the way each item was presented to her leaked a scoring-relevant fact.
  See **L4-L8**.
- The `G1` ratings were produced in the same context that authored the items, so
  they are not independent. That pilot pass has been superseded by two independent
  API passes (`G2`, `G4`), is excluded from every headline statistic, and is
  retained on the record. See **L1**.
- The judge runs are **not bit-reproducible**: the models used reject the
  `temperature` parameter. The test-retest arm measures the resulting variance
  (0.86-1.00 weighted kappa within a judge) rather than assuming it away, but
  sensitivity to the *wording* of the rubric is untested. See **L3** and
  `docs/run_log.md`.
- **The cross-vendor arm is one model from one other vendor.** `G5` (an OpenAI
  model) has been run over all 40 items and is in the independent panel, so the
  cross-vendor capability is a result rather than a promise. But with one model per
  vendor the design **cannot separate a vendor effect from a model effect**, and no
  third vendor has been run. See **L14**.
- **The ranking within the strong judges is not established.** `G5` and `G4` differ
  by one item out of the fifteen the human scored; the paired bootstrap on that
  difference spans zero. Section 3a of the report states this next to the point
  estimates. See **L8**.
