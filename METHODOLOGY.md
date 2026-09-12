# Measuring whether two AI judges agree about legal answers

A small, complete evaluation study: 40 legal questions, a written rubric, a system
under test, two independent model judges, and the inter-rater statistics that say
whether the judges are measuring the same thing.

---

## The question

Any evaluation programme that scores model output with model judges rests on an
assumption that is almost never tested before it is relied on: that a different
judge, applying the same rubric to the same output, would reach the same score.
If that fails, every downstream number — pass rates, regression checks, release
gates — is a property of the judge rather than of the system.

This study measures it on a legal question set, and reports what broke.

## Design

**Items (40).** Authored for this study across eight practice areas: commercial
contracts including UCC (7), corporate / M&A / tax / antitrust (7), employment
(6), litigation procedure, e-discovery and privilege (6), data privacy and
regulatory including AI and securities disclosure (6), IP and trade secrets (4),
real estate (2), legal ethics (2). Twenty-four are US-federal, US-general or
multi-state; sixteen are tied to a named jurisdiction — Delaware (5), California
(5), New York (2), the EU (3), England and Wales (1) — because jurisdiction
substitution is one of the failure modes under test.

Each item carries a **gold reference**: the material points a competent answer
must cover, the specific **trap** the item is built around, and the authorities a
practitioner would expect to see. The traps are the design work. They are drawn
from places where the intuitive answer is wrong or stale — a reverse triangular
merger is *not* an assignment by operation of law under Delaware law
(*Meso Scale v. Roche*); Rule 37(e)(2) requires **intent** to deprive, so
negligence does not support an adverse-inference instruction; Item 1.05 of Form
8-K runs four business days from the **materiality determination**, not from the
incident; a confidential sale still triggers the on-sale bar after *Helsinn*;
California's market-out exception is itself subject to an exception that restores
appraisal rights in a cash-out merger. An item without a trap measures nothing:
every judge agrees on an easy answer.

**System under test.** A Haiku-class model, run in a cold context with no access
to the gold references, under two documented prompt conditions: `A_standard`
(normal assistant framing) and `B_terse` ("the user is an experienced lawyer who
finds hedging annoying; under 80 words; no disclaimers"). Twenty items each,
assigned deterministically and balanced across practice area and difficulty.
Median length came out at 117 words under A and 32 under B — the manipulation
took. `B_terse` is not a straw man; it is the prompt a product team writes when
users complain the assistant hedges too much.

**Rubric.** Five ordinal 0–3 dimensions with behavioural anchors — legal
accuracy, jurisdictional grounding, issue completeness, authority hygiene, scope
discipline — plus a binary critical-failure flag covering fabricated authority,
confidently inverted rules, jurisdiction substitution, and missed dispositive
deadlines. Explicit adjudication rules: score the answer as written, tie-break
downward, rationale mandatory, length is not quality. Full text in
`docs/rubric.md`.

**Judges.** Eight rating passes in total. Four form the panel:

| Rater | Model | Items | Execution |
|---|---|---|---|
| `G2` | Sonnet-class | 40 | API, one independent call per item |
| `G4` | Opus-class | 40 | API, one independent call per item |
| `G3` | Haiku-class | 40 | cold subagent, fresh context |
| `GH` | **human** | 15 | manual, one item at a time |
| `G1` | Opus-class | 40 | pilot pass in the authoring context - **excluded from the headline** |

Three further passes are control arms rather than panel members: `G4b` and `G2b`
repeat `G4` and `G2` with the same prompt in a different order (test-retest), and
`G4ng` repeats `G4` with the gold reference removed (ablation).

Each judge saw only the rubric, the item, the gold reference and the answer:
never the generation condition, the authored difficulty, or another judge's
output. `G1` ran in the same context that wrote the items, so it knew what each
trap was designed to catch; it is retained for comparison and excluded from every
multi-rater statistic.

**The human rater is a non-expert applying the rubric, not a legal expert.** She
scored 15 of the 40 items - one drawn at random from every practice-area x
prompt-condition stratum, plus the single highest-disagreement item, selected by
`src/sample_human_items.py` before any of her ratings were seen. She judged
whether each answer matched a written gold reference; she did **not** validate
that the gold references state the law correctly. That distinction matters and is
kept explicit throughout: it makes her pass an answer to the question a real
annotation programme actually faces - *can a trained non-expert, given a good
gold reference, reach the same verdict as a model judge?* - and not a claim to
legal ground truth.

**Statistics.** Percent exact and within-one agreement; Cohen's kappa, unweighted
and quadratically weighted (the scale is ordinal, so a 3-vs-0 split should not
count the same as a 3-vs-2); Gwet's AC1/AC2, because kappa's chance correction
collapses when the marginals are skewed and this set skews hard on two
dimensions; percentile bootstrap CIs over items, 5,000 resamples. Fleiss' kappa
and Krippendorff's alpha (ordinal) over the independent panel. Every estimator is implemented from scratch in `src/agreement.py` and
validated in `tests/` against published worked examples and against the
`scikit-learn` and `krippendorff` reference implementations.

## Findings

**1. The disagreement is real, not run-to-run noise.** This has to come first,
because it is what licenses every other finding. Each judge was run a second time
on the same items with the same prompt. Weighted kappa **with itself** was 0.86 to
1.00 for the Opus-class judge and 0.71 to 0.95 for the Sonnet-class judge; on the
critical-failure flag the Opus judge reproduced its 18 flags **exactly**
(kappa 1.00). Against *each other*, the same two judges reach 0.31 to 0.78. A
judge that agrees with itself at 1.00 and with its neighbour at 0.24 is not noisy
- it is systematically different, and re-running will not average that away.
Worth noting because these models reject the `temperature` parameter, so the runs
could not be pinned to deterministic sampling; the retest arm is what establishes
the stability empirically rather than assuming it.

**2. The choice of judge dominates everything else.** Across the panel, the share
of answers flagged as a critical failure - the deployment gate - ran from **8% to
75%**. Mean legal-accuracy score ran from **1.07 to 2.50** on a 0-3 scale. Same
rubric, same answers, same instructions.

**3. Matching a judge to a human by average score picks the wrong judge.** The
human rater's mean legal-accuracy score is **1.07** - identical to the
Sonnet-class judge (1.07) and well below the Opus-class judge (1.43). On
aggregate severity, Sonnet is the perfect match. Item by item it is not close:

| Against the human rater (n=15) | Opus-class | Sonnet-class | Haiku-class |
|---|---|---|---|
| Critical-failure flag (kappa) | **0.62** | 0.24 | **0.00** |
| Jurisdictional grounding (kappa_w) | 0.62 | 0.57 | 0.00 |
| Issue completeness (kappa_w) | 0.67 | 0.63 | 0.01 |
| Legal accuracy (kappa_w) | 0.58 | 0.47 | 0.10 |

The low-cost judge flagged **none** of the nine items the human flagged as
critical failures - zero of nine. And the Opus judge produced **no false
positives at all** against the human: every item it flagged, she flagged too; it
only missed three. For a release gate, that asymmetry is the property worth
knowing, and it is invisible in any aggregate score.

**4. Agreement is worst on the two things a legal product most needs.** Even
between the two strong model judges, the critical-failure flag reached kappa
**0.24** and authority hygiene - the dimension that catches fabricated citations
- reached weighted kappa **0.31**, the lowest of the five.

**5. Roughly a third of the agreement was the answer key, not the law.** Removing
the gold reference from the Opus judge's prompt dropped its agreement with its own
gold-reference-equipped self from a 0.86-1.00 ceiling to **0.46-0.75**. The
collapse is worst on authority hygiene: **1.00 to 0.46**. That is the expected
place for it - without a list of expected authorities, "should a citation have
been here?" becomes a judgment call rather than a lookup - and it is direct
evidence for proposal P4, which makes that dimension conditional on an authored
`citation_expected` flag. The flag itself held up better (kappa 0.64, and 19
flags against 18), and the no-gold judge still agreed with the human better than
the Sonnet judge did with the answer key in hand (0.47 vs 0.24).

**6. The failure mode is instrument design, not legal reading.** On most items
where a stricter judge flagged and a lenient one did not, the lenient judge's own
rationale had already named the defect - "Misstates vehicle as Rule 12(e) when
correct answer is Rule 12(c)", "Fails to address DGCL 251(h)... major omission" -
and then did not set the flag. Replacing the holistic flag with four independent
binary checks is proposal P1. Without mandatory rationales this would have been
invisible: kappa alone says "the raters disagree" and implies the raters are the
problem.

**7. Kappa alone would have produced the wrong diagnosis on jurisdiction.** `G1`
vs `G3` showed **100% agreement within one point** on jurisdictional grounding
with weighted kappa of **0.09** and Gwet's AC2 of **0.89** - the kappa paradox,
traceable to a single line of the rubric (adjudication rule 3) that one judge
applied and the other did not. Gwet's coefficient is in the report for exactly
this reason.

**8. The rubric detects the manipulation, with one honest anomaly.** All judges
scored `B_terse` lower on issue completeness and scope discipline. But two scored
it *higher* on legal accuracy (+0.25). The likely explanation is mechanical: a
32-word answer makes fewer legal propositions than a 117-word one, so it has less
surface on which to be wrong. That is a defect in how D1 is defined, and the
second motivation for splitting D1 into conclusion and reasoning (P2).

## Limitations

- **L1 - the pilot pass was not independent, and is on the record rather than
  deleted.** `G1` ran in the context that authored the items. It is excluded from
  every headline statistic, retained for comparison, and marked as
  non-independent in the rater manifest. The headline judges are independent API
  passes, one call per item.
- **L2 - `G3` shares a model family with the system under test**, so its leniency
  is confounded with self-preference. The size of that effect is not separable
  from the capability difference with the data collected here.
- **L3 - sampling could not be pinned, but stability was measured instead.** The
  judge models reject the `temperature` parameter, so runs are not
  bit-reproducible. The test-retest arm (finding 1) measures the resulting
  variance directly and finds it small relative to between-judge divergence.
  Measured, not assumed - but it is measured on one repeat, not a distribution.
- **L4 - the human rater is a non-expert.** She validates that the rubric is
  applicable and consistent against a written gold reference. She does **not**
  validate that the gold references state the law correctly. Nothing here
  establishes legal ground truth.
- **L5 - the human pass covers 15 items, and one of her dimensions has almost no
  variance.** She scored issue completeness 1 on 14 of 15 items. Kappa is
  unstable at that marginal distribution - Gwet's AC2 on the same cells is 0.99 -
  so her D3 figures should be read as weak evidence, and the comparison across
  judges on D3 rests mostly on the model arms.
- **L6 - n = 40 (15 for the human), and roughly forty pairwise coefficients are
  reported with no multiplicity control.** Bootstrap CIs on weighted kappa run
  about +/-0.2 at n=40 and wider at n=15. Directions are stable across resamples;
  the precise ranking of dimensions is not.
- **L7 - items are authored, not sampled.** Every item is built around a trap, so
  the observed critical-failure rates say nothing about the rate a production
  system would show on real traffic. They are a stress test, not a survey.
- **L8 - single vendor.** All model judges are Claude models. Cross-vendor
  agreement is the more demanding test, and `run_graders.py` supports OpenAI and
  Google providers for it.
- **L9 - the prompt-condition manipulation is confounded.** `B_terse` changes
  length, hedging and directness at once, so an effect cannot be attributed to
  one of them. The mechanical explanation offered for the D1 anomaly in finding 8
  is a hypothesis, not a tested result.
- **L10 - the gold references have not been reviewed by a licensed attorney.**
  They are researched against named primary authority and re-checked against
  primary sources in September 2026 (`docs/verification.md`), but in a production
  programme they would be adjudicated by subject-matter experts. Several items are
  deliberately built on rules that change - HSR thresholds, FLSA salary levels, EU
  AI Act application dates - and reward an answer that flags the volatility rather
  than one that states a figure.

## What this cost

One person, roughly a week: two days authoring items and gold references, one day
on the rubric, one on the harness and statistics, one on the analysis and
write-up. The expensive part was the gold references, and that is where it should
be — the rest of the pipeline is worth nothing without them.

## Reproducing

```bash
pip install -r requirements.txt
python tests/test_agreement.py        # validate the statistics
python src/analyze.py                 # rebuild the report from data/grades/
python src/figures.py                 # rebuild the figures
```

Adding a judge or a human rater, and re-running with independent API calls, is
documented in `README.md`.
