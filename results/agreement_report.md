# Inter-rater agreement report

Generated from `data/grades/` by `src/analyze.py`. 40 items scored by 8 rater(s): `G1` (Opus-class, in-session), `G2` (Sonnet-class, API), `G2b` (Sonnet-class, API, second run), `G3` (Haiku-class, cold subagent), `G4` (Opus-class, API), `G4b` (Opus-class, API, second run), `G4ng` (Opus-class, API, gold reference withheld), `GH` (Non-expert human rater, rubric-trained).

> **Excluded from the headline figures:** `G1`, `G2b`, `G4b`, `G4ng`. Their ratings remain in `data/grades/` and in the pairwise tables below, but every multi-rater statistic is computed over the independent raters only. The reason is in the panel table.

> **Headline pair:** `G2` vs `G4` - the two independent, high-capability judges. The disagreement dossier and the concentration analysis use this pair.

## 1. Rater panel

| Rater | Model | Items | Execution | Independence |
|---|---|---|---|---|
| `G1` | claude-opus-5 | 40/40 | main session, all 40 items in one context | NOT independent - same context that authored the items and gold references |
| `G2` | claude-sonnet-5 | 40/40 | API, one independent call per item, extended thinking disabled, own presentation order | independent - fresh context per item, no access to other raters or to item authoring |
| `G2b` | claude-sonnet-5 | 40/40 | API, one independent call per item, different presentation order, same prompt | repeat of G2 - measures intra-rater (test-retest) reliability, not between-rater |
| `G3` | claude-haiku | 40/40 | cold subagent, fresh context, rubric + items only | independent of every other rater and of item authoring |
| `G4` | claude-opus-5 | 40/40 | API, one independent call per item, extended thinking disabled, own presentation order | independent - fresh context per item, no access to other raters or to item authoring |
| `G4b` | claude-opus-5 | 40/40 | API, one independent call per item, different presentation order, same prompt | repeat of G4 - measures intra-rater (test-retest) reliability, not between-rater |
| `G4ng` | claude-opus-5 | 39/40 | API, one independent call per item, gold reference removed from the prompt | ablation of G4 - measures how much of the agreement the answer key was doing |
| `GH` | human | 15/40 | manual, 15 of 40 items, one item at a time, no other rater's scores shown | independent; does NOT validate the legal correctness of the gold references |

## 2. Rater severity

Mean score per dimension (0-3) and share of records flagged as a critical failure.

| Rater | D1 Legal accuracy | D2 Jurisdictional grounding | D3 Issue completeness | D4 Authority hygiene | D5 Scope discipline | Critical-failure rate | n |
|---|---|---|---|---|---|---|---|
| `G1` | 1.68 | 2.40 | 1.43 | 1.35 | 1.98 | 28% | 40 |
| `G2` | 1.07 | 1.90 | 0.88 | 0.60 | 1.15 | 75% | 40 |
| `G2b` | 1.10 | 1.93 | 0.95 | 0.65 | 1.18 | 72% | 40 |
| `G3` | 2.50 | 2.92 | 1.93 | 1.30 | 2.52 | 8% | 40 |
| `G4` | 1.43 | 1.80 | 1.00 | 1.00 | 1.25 | 45% | 40 |
| `G4b` | 1.43 | 1.85 | 0.97 | 1.00 | 1.30 | 45% | 40 |
| `G4ng` | 1.28 | 1.87 | 1.05 | 1.10 | 1.28 | 49% | 39 |
| `GH` | 1.07 | 1.67 | 0.93 | 1.13 | 1.13 | 60% | 15 |

> Across 8 judges applying the same rubric to the same 40 answers, the critical-failure rate runs from **8%** (`G3`) to **75%** (`G2`) - a factor of 10. Mean legal-accuracy score spans 1.07 to 2.50 on a 0-3 scale. The choice of judge, not the system under test, is the dominant term in what gets reported.

## 3. Pairwise agreement, by dimension

`kappa` = Cohen's kappa (unweighted). `kappa_w` = quadratically weighted, which is the appropriate headline for an ordinal scale because it penalises a 3-vs-0 disagreement more than a 3-vs-2. `AC2` = Gwet's weighted agreement coefficient, reported because kappa is unstable when one category dominates the marginals. 95% CIs are percentile bootstrap over items (5,000 resamples).

### `G1` vs `G2`  (n = 40)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 42% | 98% | 0.226 | 0.675 | [0.54, 0.77] | 0.765 | substantial |
| D2 Jurisdictional grounding | 42% | 98% | -0.139 | 0.167 | [0.00, 0.28] | 0.869 | slight |
| D3 Issue completeness | 45% | 100% | 0.135 | 0.479 | [0.25, 0.66] | 0.866 | moderate |
| D4 Authority hygiene | 32% | 92% | 0.015 | 0.392 | [0.21, 0.55] | 0.746 | fair |
| D5 Scope discipline | 30% | 88% | 0.026 | 0.380 | [0.22, 0.53] | 0.661 | fair |
| **Critical-failure flag** (binary) | 52% | - | 0.224 | - | - | 0.051 | fair |

Confusion on the flag: both raised **11**, only `G1` **0**, only `G2` **19**, neither **10**.

### `G1` vs `G3`  (n = 40)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 45% | 72% | 0.243 | 0.244 | [0.06, 0.46] | 0.492 | fair |
| D2 Jurisdictional grounding | 42% | 100% | 0.050 | 0.094 | [0.00, 0.24] | 0.888 | slight |
| D3 Issue completeness | 50% | 90% | 0.199 | 0.282 | [0.04, 0.52] | 0.788 | fair |
| D4 Authority hygiene | 40% | 90% | 0.108 | 0.244 | [0.01, 0.46] | 0.736 | fair |
| D5 Scope discipline | 38% | 92% | 0.044 | 0.245 | [0.06, 0.43] | 0.768 | fair |
| **Critical-failure flag** (binary) | 70% | - | 0.028 | - | - | 0.578 | slight |

Confusion on the flag: both raised **1**, only `G1` **10**, only `G3` **2**, neither **27**.

### `G1` vs `G4`  (n = 40)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 70% | 100% | 0.574 | 0.826 | [0.71, 0.90] | 0.898 | almost perfect |
| D2 Jurisdictional grounding | 42% | 98% | -0.065 | 0.198 | [0.05, 0.32] | 0.864 | slight |
| D3 Issue completeness | 57% | 100% | 0.289 | 0.514 | [0.21, 0.72] | 0.905 | moderate |
| D4 Authority hygiene | 65% | 95% | 0.247 | 0.333 | [0.06, 0.58] | 0.906 | fair |
| D5 Scope discipline | 30% | 98% | -0.007 | 0.496 | [0.34, 0.60] | 0.765 | moderate |
| **Critical-failure flag** (binary) | 78% | - | 0.529 | - | - | 0.582 | moderate |

Confusion on the flag: both raised **10**, only `G1` **1**, only `G4` **8**, neither **21**.

### `G1` vs `GH`  (n = 15)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 33% | 100% | 0.026 | 0.561 | [0.18, 0.74] | 0.801 | moderate |
| D2 Jurisdictional grounding | 33% | 93% | 0.057 | 0.316 | [0.05, 0.55] | 0.758 | fair |
| D3 Issue completeness | 53% | 100% | 0.167 | 0.286 | [0.00, 0.59] | 0.908 | fair |
| D4 Authority hygiene | 67% | 93% | 0.324 | 0.231 | [0.00, 0.71] | 0.895 | fair |
| D5 Scope discipline | 33% | 80% | 0.107 | 0.000 | [-0.07, 0.15] | 0.687 | slight |
| **Critical-failure flag** (binary) | 67% | - | 0.390 | - | - | 0.345 | fair |

Confusion on the flag: both raised **4**, only `G1` **0**, only `GH` **5**, neither **6**.

### `G2` vs `G3`  (n = 40)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 5% | 65% | -0.097 | 0.205 | [0.08, 0.34] | 0.011 | slight |
| D2 Jurisdictional grounding | 10% | 88% | 0.007 | 0.127 | [-0.01, 0.34] | 0.685 | slight |
| D3 Issue completeness | 15% | 80% | -0.071 | 0.208 | [0.08, 0.35] | 0.580 | slight |
| D4 Authority hygiene | 28% | 88% | 0.000 | 0.286 | [0.12, 0.45] | 0.658 | fair |
| D5 Scope discipline | 8% | 52% | -0.080 | 0.089 | [-0.00, 0.17] | 0.126 | slight |
| **Critical-failure flag** (binary) | 32% | - | 0.053 | - | - | -0.310 | slight |

Confusion on the flag: both raised **3**, only `G2` **27**, only `G3` **0**, neither **10**.

### `G2` vs `G4`  (n = 40)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 55% | 100% | 0.361 | 0.716 | [0.60, 0.80] | 0.850 | substantial |
| D2 Jurisdictional grounding | 75% | 100% | 0.357 | 0.510 | [0.21, 0.70] | 0.956 | moderate |
| D3 Issue completeness | 88% | 100% | 0.652 | 0.783 | [0.40, 0.94] | 0.979 | substantial |
| D4 Authority hygiene | 55% | 100% | 0.207 | 0.308 | [0.04, 0.53] | 0.908 | fair |
| D5 Scope discipline | 65% | 100% | 0.429 | 0.659 | [0.41, 0.82] | 0.905 | substantial |
| **Critical-failure flag** (binary) | 60% | - | 0.238 | - | - | 0.231 | fair |

Confusion on the flag: both raised **16**, only `G2` **14**, only `G4` **2**, neither **8**.

### `G2` vs `GH`  (n = 15)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 40% | 100% | 0.049 | 0.471 | [0.00, 0.69] | 0.835 | moderate |
| D2 Jurisdictional grounding | 67% | 100% | 0.449 | 0.571 | [0.15, 0.86] | 0.920 | moderate |
| D3 Issue completeness | 93% | 100% | 0.634 | 0.634 | [0.00, 1.00] | 0.991 | substantial |
| D4 Authority hygiene | 53% | 100% | -0.105 | 0.160 | [0.00, 0.24] | 0.918 | slight |
| D5 Scope discipline | 67% | 100% | 0.157 | 0.257 | [-0.10, 0.67] | 0.942 | fair |
| **Critical-failure flag** (binary) | 67% | - | 0.242 | - | - | 0.425 | fair |

Confusion on the flag: both raised **8**, only `G2` **4**, only `GH` **1**, neither **2**.

### `G3` vs `G4`  (n = 40)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 28% | 70% | 0.084 | 0.235 | [0.08, 0.41] | 0.373 | fair |
| D2 Jurisdictional grounding | 8% | 80% | 0.028 | 0.044 | [-0.02, 0.16] | 0.602 | slight |
| D3 Issue completeness | 22% | 85% | -0.019 | 0.197 | [0.05, 0.36] | 0.677 | slight |
| D4 Authority hygiene | 30% | 95% | -0.037 | -0.000 | [-0.12, 0.13] | 0.801 | poor |
| D5 Scope discipline | 10% | 65% | -0.078 | 0.140 | [0.06, 0.23] | 0.298 | slight |
| **Critical-failure flag** (binary) | 57% | - | 0.071 | - | - | 0.306 | slight |

Confusion on the flag: both raised **2**, only `G3` **1**, only `G4` **16**, neither **21**.

### `G3` vs `GH`  (n = 15)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 13% | 40% | 0.015 | 0.096 | [0.00, 0.23] | -0.036 | slight |
| D2 Jurisdictional grounding | 13% | 53% | 0.000 | 0.000 | [0.00, 0.00] | 0.424 | slight |
| D3 Issue completeness | 20% | 67% | 0.016 | 0.005 | [-0.04, 0.03] | 0.538 | slight |
| D4 Authority hygiene | 53% | 100% | 0.198 | 0.234 | [0.00, 0.55] | 0.902 | fair |
| D5 Scope discipline | 7% | 53% | 0.005 | -0.004 | [-0.09, 0.08] | 0.305 | poor |
| **Critical-failure flag** (binary) | 40% | - | 0.000 | - | - | -0.034 | slight |

Confusion on the flag: both raised **0**, only `G3` **0**, only `GH` **9**, neither **6**.

### `G4` vs `GH`  (n = 15)

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 47% | 100% | 0.178 | 0.580 | [0.17, 0.79] | 0.852 | moderate |
| D2 Jurisdictional grounding | 73% | 100% | 0.538 | 0.625 | [0.31, 0.89] | 0.937 | substantial |
| D3 Issue completeness | 93% | 100% | 0.643 | 0.667 | [0.00, 1.00] | 0.991 | substantial |
| D4 Authority hygiene | 87% | 100% | 0.000 | 0.000 | [0.00, 0.00] | 0.983 | slight |
| D5 Scope discipline | 67% | 100% | 0.118 | 0.118 | [-0.26, 0.59] | 0.943 | slight |
| **Critical-failure flag** (binary) | 80% | - | 0.615 | - | - | 0.600 | substantial |

Confusion on the flag: both raised **6**, only `G4` **0**, only `GH` **3**, neither **6**.


## 4. Multi-rater agreement

Computed over the independent raters: `G2`, `G3`, `G4`, `GH`. Krippendorff's alpha uses every rating, including raters who covered only part of the set - handling missing cells natively is why it is the right headline statistic here. Fleiss' kappa requires complete cases and is computed over `G2`, `G3`, `G4` on all 40 items.

| Dimension | Fleiss kappa (complete cases) | Krippendorff alpha (ordinal, all ratings) |
|---|---|---|
| D1 Legal accuracy | 0.034 | 0.257 |
| D2 Jurisdictional grounding | -0.163 | -0.056 |
| D3 Issue completeness | -0.028 | 0.118 |
| D4 Authority hygiene | -0.054 | 0.173 |
| D5 Scope discipline | -0.029 | 0.026 |
| **Critical-failure flag** | -0.023 | 0.067 |

Per-item spread on the critical-failure flag across the 3 independent judges who scored every item:

| Judges flagging the item | Items |
|---|---|
| 0 of 3 | 8 |
| 1 of 3 | 15 |
| 2 of 3 | 15 |
| 3 of 3 | 2 |

> Unanimity - all 3 agreeing that an item is or is not a critical failure - covers **10 of 40** items.

## 4a. Intra-rater reliability (test-retest)

The same judge, the same prompt, a second independent run in a different presentation order. This separates two things that a between-rater number cannot: how much a judge disagrees **with itself** (instrument noise) and how much judges disagree **with each other** (real, systematic divergence). It matters here because these models reject the `temperature` parameter, so the runs could not be pinned to deterministic sampling.

| Judge | Legal accuracy | Jurisdictional grounding | Issue completeness | Authority hygiene | Scope discipline | Critical-failure flag | n |
|---|---|---|---|---|---|---|---|
| `G2` vs `G2b` | 0.95 | 0.71 | 0.88 | 0.94 | 0.88 | 0.94 | 40 |
| `G4` vs `G4b` | 1.00 | 0.87 | 0.86 | 1.00 | 0.89 | 1.00 | 40 |

> Read this against section 3. Where a judge agrees with **itself** far more than it agrees with any other judge, the between-rater disagreement is not run-to-run noise - it is a stable property of the judge, and no amount of re-running will average it away.

## 4b. Ablation - gold reference withheld

Every judge in section 3 was shown the item's gold reference: the material points, the trap, and the authorities a practitioner would expect. That makes part of the task 'match the answer key'. This arm re-runs one judge with the gold reference removed, so it must rely on its own legal knowledge. The drop measures how much of the reported agreement the answer key was carrying.

| Comparison | Legal accuracy | Jurisdictional grounding | Issue completeness | Authority hygiene | Scope discipline | Critical-failure flag | n |
|---|---|---|---|---|---|---|---|
| `G4` vs `G4ng` - gold withheld | 0.75 | 0.67 | 0.73 | 0.46 | 0.64 | 0.64 | 39 |
| `G4` vs `G4b` - same prompt (ceiling) | 1.00 | 0.87 | 0.86 | 1.00 | 0.89 | 1.00 | 40 |

## 5. Does the rubric detect the manipulation?

The 40 answers were generated under two prompt conditions: `A_standard` and `B_terse` (direct, no caveats, under 80 words). If the rubric measures anything real, both judges should score `B_terse` lower on completeness. This is a construct-validity check on the rubric, independent of whether the judges agree with each other.

| Rater | Dimension | A_standard | B_terse | Delta |
|---|---|---|---|---|
| `G1` | D1 Legal accuracy | 1.55 | 1.80 | +0.25 |
| `G1` | D2 Jurisdictional grounding | 2.35 | 2.45 | +0.10 |
| `G1` | D3 Issue completeness | 1.55 | 1.30 | -0.25 |
| `G1` | D4 Authority hygiene | 1.50 | 1.20 | -0.30 |
| `G1` | D5 Scope discipline | 2.05 | 1.90 | -0.15 |
| `G2` | D1 Legal accuracy | 1.10 | 1.05 | -0.05 |
| `G2` | D2 Jurisdictional grounding | 1.85 | 1.95 | +0.10 |
| `G2` | D3 Issue completeness | 1.00 | 0.75 | -0.25 |
| `G2` | D4 Authority hygiene | 0.80 | 0.40 | -0.40 |
| `G2` | D5 Scope discipline | 1.25 | 1.05 | -0.20 |
| `G2b` | D1 Legal accuracy | 1.10 | 1.10 | +0.00 |
| `G2b` | D2 Jurisdictional grounding | 1.95 | 1.90 | -0.05 |
| `G2b` | D3 Issue completeness | 1.05 | 0.85 | -0.20 |
| `G2b` | D4 Authority hygiene | 0.80 | 0.50 | -0.30 |
| `G2b` | D5 Scope discipline | 1.35 | 1.00 | -0.35 |
| `G3` | D1 Legal accuracy | 2.65 | 2.35 | -0.30 |
| `G3` | D2 Jurisdictional grounding | 2.95 | 2.90 | -0.05 |
| `G3` | D3 Issue completeness | 2.15 | 1.70 | -0.45 |
| `G3` | D4 Authority hygiene | 1.80 | 0.80 | -1.00 |
| `G3` | D5 Scope discipline | 2.75 | 2.30 | -0.45 |
| `G4` | D1 Legal accuracy | 1.30 | 1.55 | +0.25 |
| `G4` | D2 Jurisdictional grounding | 1.70 | 1.90 | +0.20 |
| `G4` | D3 Issue completeness | 1.10 | 0.90 | -0.20 |
| `G4` | D4 Authority hygiene | 1.00 | 1.00 | +0.00 |
| `G4` | D5 Scope discipline | 1.40 | 1.10 | -0.30 |
| `G4b` | D1 Legal accuracy | 1.30 | 1.55 | +0.25 |
| `G4b` | D2 Jurisdictional grounding | 1.75 | 1.95 | +0.20 |
| `G4b` | D3 Issue completeness | 1.05 | 0.90 | -0.15 |
| `G4b` | D4 Authority hygiene | 1.00 | 1.00 | +0.00 |
| `G4b` | D5 Scope discipline | 1.50 | 1.10 | -0.40 |
| `G4ng` | D1 Legal accuracy | 1.35 | 1.21 | -0.14 |
| `G4ng` | D2 Jurisdictional grounding | 1.85 | 1.89 | +0.04 |
| `G4ng` | D3 Issue completeness | 1.25 | 0.84 | -0.41 |
| `G4ng` | D4 Authority hygiene | 1.15 | 1.05 | -0.10 |
| `G4ng` | D5 Scope discipline | 1.45 | 1.11 | -0.34 |
| `GH` | D1 Legal accuracy | 0.75 | 1.43 | +0.68 |
| `GH` | D2 Jurisdictional grounding | 1.38 | 2.00 | +0.62 |
| `GH` | D3 Issue completeness | 1.00 | 0.86 | -0.14 |
| `GH` | D4 Authority hygiene | 1.25 | 1.00 | -0.25 |
| `GH` | D5 Scope discipline | 1.12 | 1.14 | +0.02 |

## 6. Where the disagreement is concentrated

Mean absolute per-dimension gap between `G2` and `G4`, by practice area:

| Practice area | n | Mean gap |
|---|---|---|
| Trade secrets | 1 | 0.60 |
| Data privacy | 3 | 0.40 |
| Antitrust / M&A | 1 | 0.40 |
| Litigation / e-discovery | 1 | 0.40 |
| Privilege | 1 | 0.40 |
| Real estate | 1 | 0.40 |
| Real estate / finance | 1 | 0.40 |
| Legal ethics / confidentiality | 1 | 0.40 |
| Employment | 6 | 0.40 |
| Commercial contracts | 6 | 0.37 |
| Corporate / M&A | 5 | 0.32 |
| Intellectual property | 3 | 0.27 |
| Litigation procedure | 4 | 0.25 |
| Commercial contracts (UCC) | 1 | 0.20 |
| Health data | 1 | 0.20 |
| AI regulation | 1 | 0.20 |
| Legal ethics / UPL | 1 | 0.20 |
| Corporate / tax | 1 | 0.00 |
| Securities / cyber | 1 | 0.00 |

By authored difficulty:

| Difficulty | n | Mean gap |
|---|---|---|
| 2 | 19 | 0.36 |
| 3 | 21 | 0.30 |

