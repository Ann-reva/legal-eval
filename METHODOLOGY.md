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

**Judges.** Two model judges scored all 40 items, each in its own presentation
order, seeing only the rubric, the item, the gold reference and the answer:
`G1` (Opus-class) and `G3` (Haiku-class, the low-cost arm). Neither saw the
other's output or the generation condition. A human rating pass is supported by
the harness and has not been run — see L4.

**Statistics.** Percent exact and within-one agreement; Cohen's kappa, unweighted
and quadratically weighted (the scale is ordinal, so a 3-vs-0 split should not
count the same as a 3-vs-2); Gwet's AC1/AC2, because kappa's chance correction
collapses when the marginals are skewed and this set skews hard on two
dimensions; percentile bootstrap CIs over items, 5,000 resamples. Fleiss' kappa
and Krippendorff's alpha (ordinal) compute automatically once a third rater
exists. Every estimator is implemented from scratch in `src/agreement.py` and
validated in `tests/` against published worked examples and against the
`scikit-learn` and `krippendorff` reference implementations.

## Findings

**1. The two judges do not agree, on any dimension.** Weighted kappa ranged from
0.09 to 0.28 — "slight" to "fair". Exact agreement was 38–50%. The bootstrap CIs
are wide (typically ±0.2) at n = 40, so the precise values should not be
over-read; the conclusion that none of them is near an acceptable threshold is
robust to that width.

**2. Agreement was worst on the dimension that matters most.** The
critical-failure flag — the deployment gate — reached Cohen's kappa **0.03**,
indistinguishable from chance. `G1` flagged 11 items, `G3` flagged 3, and they
overlapped on **1**. A team that swapped judges would see its blocker count move
by a factor of three.

**3. The failure was in the instrument, not the rater's legal reading.** This is
the result that changes what to do about it. On most items where only `G1`
flagged, `G3`'s own free-text rationale had already identified the defect — "Misstates
vehicle as Rule 12(e) when correct answer is Rule 12(c)", "Fails to address DGCL
251(h)… major omission", "Violates rubric guidance by asserting specific 2024
threshold as settled law" — and then did not set the flag. The rater diagnosed
correctly and failed to map the diagnosis onto a holistic yes/no. That is fixable
by replacing the holistic flag with four independent binary checks, which is
proposal P1 in `results/rubric_v1.1_proposal.md`. Without mandatory rationales
this would have been invisible: the kappa alone says "raters disagree" and
implies the raters are the problem.

**4. Kappa alone would have produced the wrong diagnosis on D2.** Jurisdictional
grounding showed **100% agreement within one point** and weighted kappa of
**0.09** — while Gwet's AC2 was **0.89**. The cause is traceable to a single
line in the rubric (adjudication rule 3, "if a dimension is barely engaged, score
it 2") that one judge applied and the other did not, pushing almost all the mass
into two adjacent cells. Reporting kappa alone would have sent effort at a
rater-calibration problem that does not exist.

**5. The low-cost judge is usable for ranking and not for gating.** It was
0.82 points more lenient on legal accuracy (2.50 vs 1.68 on a 0–3 scale) and
caught 1 of 11 critical failures. But it ordered the two prompt conditions
correctly and more sharply than the expensive judge did — `B_terse` scored
−1.00 on authority hygiene and −0.45 on completeness. A cheap judge whose bias is
roughly constant still detects *relative* movement; it cannot be trusted with an
absolute safety threshold. Proposal P6 turns that into a two-tier routing rule.

**6. The rubric detects the manipulation, with one honest anomaly.** Both judges
scored `B_terse` lower on completeness, authority hygiene and scope discipline —
the rubric measures something real. But `G1` scored `B_terse` *higher* on legal
accuracy (+0.25). The likely explanation is mechanical rather than flattering to
the terse condition: a 32-word answer makes fewer legal propositions than a
117-word one, so it has less surface on which to be wrong. That is a defect in
how D1 is defined, not evidence that terse answers are more accurate, and it is
the second motivation for splitting D1 into conclusion and reasoning (P2).

## Limitations

These are the reasons not to over-read the numbers above. They are listed because
an evaluation write-up that does not list them is not finished.

- **L1 — `G1` is not independent of item authoring.** It ran in the same context
  that wrote the questions and gold references, so it knew what each trap was
  designed to catch. This inflates its apparent severity and is the single
  largest threat to the reported figures. `src/run_graders.py` fixes it: one
  independent API call per item, temperature 0, fresh context. Re-running with
  two API judges is the first thing to do with this repository.
- **L2 — `G3` shares a model family with the system under test**, so its leniency
  is confounded with self-preference. The size of that effect is not separable
  from the capability difference with the data collected here.
- **L3 — n = 40.** Bootstrap CIs on weighted kappa run roughly ±0.2. The
  direction of every finding is stable across resamples; the point estimates are
  not precise.
- **L4 — no human rater.** Without one there is no anchor for which judge is
  closer to right, only a measure of whether they agree. The harness supports a
  human pass (`src/human_sheet.py`), including a partial one.
- **L5 — single vendor.** Both judges are Claude models. Cross-vendor agreement
  is the more demanding and more informative test, and `run_graders.py` supports
  OpenAI and Google providers for exactly that.
- **L6 — the gold references were authored for this study and have not been
  reviewed by a licensed attorney.** They are researched against named primary
  authority and are, to the author's knowledge, accurate as of September 2026,
  but in a production programme they would be adjudicated by subject-matter
  experts before any score derived from them was relied on. Several items are
  deliberately built on rules that change — HSR thresholds, FLSA salary levels,
  EU AI Act application dates — and those items are designed to reward an answer
  that flags the volatility rather than one that states a figure.

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
