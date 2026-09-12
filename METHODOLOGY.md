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

**Judges.** Four rating passes over all 40 items. Three are independent and carry
the headline figures:

| Rater | Model | Execution |
|---|---|---|
| `G2` | Sonnet-class | API, one independent call per item, own presentation order |
| `G4` | Opus-class | API, one independent call per item, own presentation order |
| `G3` | Haiku-class | cold subagent, fresh context, rubric and items only |
| `G1` | Opus-class | pilot pass in the authoring context — **excluded from the headline** |

Each judge saw only the rubric, the item, the gold reference and the answer:
never the generation condition, the authored difficulty, or another judge's
output. `G1` was the first pass and ran in the same context that wrote the items,
so it knew what each trap was designed to catch. It is retained in the repository
and in the pairwise tables for comparison, and excluded from every multi-rater
statistic. A human rating pass is supported by the harness and has not been run.

**Statistics.** Percent exact and within-one agreement; Cohen's kappa, unweighted
and quadratically weighted (the scale is ordinal, so a 3-vs-0 split should not
count the same as a 3-vs-2); Gwet's AC1/AC2, because kappa's chance correction
collapses when the marginals are skewed and this set skews hard on two
dimensions; percentile bootstrap CIs over items, 5,000 resamples. Fleiss' kappa
and Krippendorff's alpha (ordinal) over the independent panel. Every estimator is implemented from scratch in `src/agreement.py` and
validated in `tests/` against published worked examples and against the
`scikit-learn` and `krippendorff` reference implementations.

## Findings

**1. The choice of judge dominates everything else.** Across the four passes, the
number of answers flagged as a critical failure — the deployment gate — ran from
**3 to 30 out of 40**. Mean legal-accuracy score ran from **1.07 to 2.50** on a
0–3 scale. Same rubric, same answers, same instructions. Whatever such a
programme reports about the system under test is, on this evidence, mostly a
report about which judge was hired.

**2. Three independent judges produce no usable multi-rater agreement at all.**
Fleiss' kappa over `G2`, `G3` and `G4` was **0.03 or below on every dimension**,
negative on three of them. Krippendorff's alpha (ordinal) peaked at **0.22** on
legal accuracy and was negative on jurisdictional grounding and scope discipline.
On the critical-failure flag, all three agreed — either that an item is a blocker
or that it is not — on **10 of 40 items**. For fifteen items exactly one of the
three raised the flag.

**3. But capability tier, not the rubric, is what breaks it.** Restricting to the
two strong independent judges, `G2` and `G4`, agreement is respectable:
weighted kappa **0.78** on issue completeness, **0.72** on legal accuracy,
**0.66** on scope discipline, **0.51** on jurisdictional grounding. The
three-rater figures collapse because the low-cost arm is a different instrument,
not because the rubric is unusable between comparable raters. That distinction is
invisible in a single Fleiss number, and it changes the recommendation
completely: the fix is judge selection and routing, not another rubric rewrite.

**4. Agreement is worst on the two things a legal product most needs.** Even
between the two strong judges, the critical-failure flag reached kappa **0.24**
and authority hygiene — the dimension that catches fabricated citations —
reached weighted kappa **0.31**, the lowest of the five. `G2` flagged 30 items,
`G4` 18, overlapping on 16: the same evidence, very different thresholds for
"this blocks release."

**5. The failure mode is instrument design, not legal reading.** On most items
where a stricter judge flagged and a lenient one did not, the lenient judge's own
free-text rationale had already named the defect — "Misstates vehicle as Rule
12(e) when correct answer is Rule 12(c)", "Fails to address DGCL 251(h)… major
omission", "Violates rubric guidance by asserting specific 2024 threshold as
settled law" — and then did not set the flag. The rater diagnosed correctly and
failed to map the diagnosis onto a holistic yes/no. Replacing the holistic flag
with four independent binary checks is proposal P1 in
`results/rubric_v1.1_proposal.md`. Without mandatory rationales this would have
been invisible: kappa alone says "the raters disagree" and implies the raters are
the problem.

**6. Kappa alone would have produced the wrong diagnosis on jurisdiction.** `G1`
vs `G3` showed **100% agreement within one point** on jurisdictional grounding
with weighted kappa of **0.09** and Gwet's AC2 of **0.89**. The cause is
traceable to a single line of the rubric — adjudication rule 3, "if a dimension is
barely engaged, score it 2" — which one judge applied and the other did not,
pushing almost all the mass into two adjacent cells. Reporting kappa alone would
have sent effort at a rater-calibration problem that does not exist. Gwet's
coefficient is in the report for exactly this reason.

**7. The rubric detects the manipulation, with one honest anomaly.** All four
judges scored `B_terse` lower on issue completeness and scope discipline, and
three of four lower on authority hygiene (`G3` by a full point). So the rubric
measures something real. But two judges scored `B_terse` *higher* on legal
accuracy (+0.25 each). The likely explanation is mechanical rather than
flattering to the terse condition: a 32-word answer makes fewer legal
propositions than a 117-word one, so it has less surface on which to be wrong.
That is a defect in how D1 is defined, not evidence that terse answers are more
accurate, and it is the second motivation for splitting D1 into conclusion and
reasoning (P2).

## Limitations

These are the reasons not to over-read the numbers above. They are listed because
an evaluation write-up that does not list them is not finished.

- **L1 — resolved, and kept on the record.** The first rating pass (`G1`) ran in
  the context that authored the items, so it was not independent. Rather than
  quietly dropping it, it is excluded from every headline statistic, retained for
  comparison, and marked as non-independent in the rater manifest. The headline
  judges are independent API passes, one call per item.
- **L2 — `G3` shares a model family with the system under test**, so its leniency
  is confounded with self-preference. The size of that effect is not separable
  from the capability difference with the data collected here.
- **L3 — sampling could not be pinned.** The models used for `G2` and `G4` reject
  the `temperature` parameter, so the runs are at each model's default sampling
  and are not bit-reproducible. Each item is still a separate request, so no
  within-run calibration is possible; but re-running will not reproduce these
  exact ratings. The harness records which sampling shape the model accepted.
- **L4 — n = 40.** Bootstrap CIs on weighted kappa run roughly ±0.2. The
  direction of every finding is stable across resamples; the point estimates are
  not precise.
- **L5 — no human rater.** Without one there is no anchor for which judge is
  closer to right, only a measure of whether they agree. Given how far apart the
  judges are, this is now the most valuable missing piece: the harness supports a
  human pass (`src/human_sheet.py`), including a partial one over 15 items.
- **L6 — single vendor.** All four judges are Claude models. Cross-vendor
  agreement is the more demanding and more informative test, and
  `run_graders.py` supports OpenAI and Google providers for exactly that.
- **L7 — the gold references were authored for this study and have not been
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
