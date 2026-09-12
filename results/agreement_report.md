# Inter-rater agreement report

Generated from `data/grades/` by `src/analyze.py`. 40 items scored by 2 rater(s): `G1` (Opus-class judge), `G3` (Haiku-class judge).

## 1. Rater panel

| Rater | Model | Execution | Independence |
|---|---|---|---|
| `G1` | claude-opus-5 | main session (same context that authored the question set and gold references) | NOT independent of the item authoring; see METHODOLOGY.md Limitations L1 |
| `G3` | claude-haiku | cold subagent, fresh context, rubric + items only | independent of G1 and of the item authoring; saw no other rater's output |

## 2. Rater severity

Mean score per dimension (0-3) and share of records flagged as a critical failure.

| Rater | D1 Legal accuracy | D2 Jurisdictional grounding | D3 Issue completeness | D4 Authority hygiene | D5 Scope discipline | Critical-failure rate |
|---|---|---|---|---|---|---|
| `G1` | 1.68 | 2.40 | 1.43 | 1.35 | 1.98 | 28% |
| `G3` | 2.50 | 2.92 | 1.93 | 1.30 | 2.52 | 8% |

> Severity gap on D1 between `G1` and `G3`: **+0.82 points on a 0-3 scale**. A gap this size means the two judges would report materially different pass rates for the same system, before any question of agreement on individual items.

## 3. Pairwise agreement, by dimension

`kappa` = Cohen's kappa (unweighted). `kappa_w` = quadratically weighted, which is the appropriate headline for an ordinal scale because it penalises a 3-vs-0 disagreement more than a 3-vs-2. `AC2` = Gwet's weighted agreement coefficient, reported because kappa is unstable when one category dominates the marginals. 95% CIs are percentile bootstrap over items (5,000 resamples).

### `G1` vs `G3`

| Dimension | Exact | Within 1 | kappa | kappa_w | 95% CI (kappa_w) | AC2 | Label (kappa_w) |
|---|---|---|---|---|---|---|---|
| D1 Legal accuracy | 45% | 72% | 0.243 | 0.244 | [0.06, 0.46] | 0.492 | fair |
| D2 Jurisdictional grounding | 42% | 100% | 0.050 | 0.094 | [0.00, 0.24] | 0.888 | slight |
| D3 Issue completeness | 50% | 90% | 0.199 | 0.282 | [0.04, 0.52] | 0.788 | fair |
| D4 Authority hygiene | 40% | 90% | 0.108 | 0.244 | [0.01, 0.46] | 0.736 | fair |
| D5 Scope discipline | 38% | 92% | 0.044 | 0.245 | [0.06, 0.43] | 0.768 | fair |
| **Critical-failure flag** (binary) | 70% | - | 0.028 | - | - | 0.578 | slight |

Confusion on the flag: both raised **1**, only `G1` **10**, only `G3` **2**, neither **27**.


## 4. Multi-rater agreement

Requires three or more raters. Add a third rating pass (`data/grades/GH.jsonl`, or a cross-vendor judge via `src/run_graders.py`) and re-run; Fleiss' kappa and Krippendorff's alpha are computed automatically.

## 5. Does the rubric detect the manipulation?

The 40 answers were generated under two prompt conditions: `A_standard` and `B_terse` (direct, no caveats, under 80 words). If the rubric measures anything real, both judges should score `B_terse` lower on completeness. This is a construct-validity check on the rubric, independent of whether the judges agree with each other.

| Rater | Dimension | A_standard | B_terse | Delta |
|---|---|---|---|---|
| `G1` | D1 Legal accuracy | 1.55 | 1.80 | +0.25 |
| `G1` | D2 Jurisdictional grounding | 2.35 | 2.45 | +0.10 |
| `G1` | D3 Issue completeness | 1.55 | 1.30 | -0.25 |
| `G1` | D4 Authority hygiene | 1.50 | 1.20 | -0.30 |
| `G1` | D5 Scope discipline | 2.05 | 1.90 | -0.15 |
| `G3` | D1 Legal accuracy | 2.65 | 2.35 | -0.30 |
| `G3` | D2 Jurisdictional grounding | 2.95 | 2.90 | -0.05 |
| `G3` | D3 Issue completeness | 2.15 | 1.70 | -0.45 |
| `G3` | D4 Authority hygiene | 1.80 | 0.80 | -1.00 |
| `G3` | D5 Scope discipline | 2.75 | 2.30 | -0.45 |

## 6. Where the disagreement is concentrated

Mean absolute per-dimension gap between `G1` and `G3`, by practice area:

| Practice area | n | Mean gap |
|---|---|---|
| Privilege | 1 | 1.40 |
| Litigation / e-discovery | 1 | 1.20 |
| Litigation procedure | 4 | 1.05 |
| Securities / cyber | 1 | 1.00 |
| Commercial contracts | 6 | 0.93 |
| AI regulation | 1 | 0.80 |
| Real estate / finance | 1 | 0.80 |
| Legal ethics / UPL | 1 | 0.80 |
| Intellectual property | 3 | 0.73 |
| Corporate / tax | 1 | 0.60 |
| Data privacy | 3 | 0.60 |
| Employment | 6 | 0.53 |
| Corporate / M&A | 5 | 0.44 |
| Antitrust / M&A | 1 | 0.40 |
| Health data | 1 | 0.40 |
| Real estate | 1 | 0.40 |
| Legal ethics / confidentiality | 1 | 0.40 |
| Commercial contracts (UCC) | 1 | 0.20 |
| Trade secrets | 1 | 0.00 |

By authored difficulty:

| Difficulty | n | Mean gap |
|---|---|---|
| 2 | 19 | 0.53 |
| 3 | 21 | 0.84 |

