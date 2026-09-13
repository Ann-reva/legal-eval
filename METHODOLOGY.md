# Do two AI judges scoring legal answers measure the same thing?

A small, complete evaluation study: 40 legal questions, a written rubric, a system
under test, four model judges across two vendors, a human rater, and the
inter-rater statistics that say whether the judges are measuring the same thing.

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

**Judges.** Nine rating passes in total. Five form the panel:

| Rater | Model | Items | Execution |
|---|---|---|---|
| `G4` | Opus-class | 40 | API, one independent call per item |
| `G5` | **GPT-class, a different vendor** | 40 | API, one independent call per item |
| `G2` | Sonnet-class | 40 | API, one independent call per item |
| `G3` | Haiku-class | 40 | cold subagent, fresh context |
| `GH` | **human** | 15 | manual, one item at a time |
| `G1` | Opus-class | 40 | pilot pass in the authoring context - **excluded from the headline** |

`G5` is the only judge with no family relationship to the system under test,
which is a Claude model. Any self-preference effect that inflates a Claude
judge's scores does not apply to it.

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

**1. The disagreement does not look like run-to-run noise.** This has to come
first, because it is what licenses every other finding. Each judge was run a
second time on the same items with the same prompt. Weighted kappa **with itself**
was 0.86 to 1.00 for the Opus-class judge and 0.71 to 0.95 for the Sonnet-class
judge; on the critical-failure flag the Opus judge reproduced its 18 flags
**exactly** (kappa 1.00). Against *each other*, the same two judges reach 0.31 to
0.78.

A judge that agrees with itself at 1.00 and with its neighbour at 0.24 is, on this
evidence, systematically different rather than noisy. The claim should be read
with two bounds on it. One repeat bounds run-to-run variance; it does not
establish the judge's behavioural distribution, which would need many repeats.
And re-running the *same* prompt tests the smaller risk - sensitivity to how the
rubric is worded and ordered is the larger one for an LLM judge, and it is
untested here (L3). What the arm does establish is that the variance these models
show without a `temperature` control is small relative to the gap between judges,
measured rather than assumed.

**2. The choice of judge dominates everything else.** Across the panel, the share
of answers flagged as a critical failure - the deployment gate - ran from **8% to
75%**. Mean legal-accuracy score ran from **0.97 to 2.50** on a 0-3 scale. Same
rubric, same answers, same instructions.

**3. In this sample, matching a judge to a human by average score would have
picked the wrong judge.** The human rater's mean legal-accuracy score is identical
to the Sonnet-class judge (1.07). Item by item it is not close:

| Against the human rater (n=15) | GPT-class (other vendor) | Opus-class | Sonnet-class | Haiku-class |
|---|---|---|---|---|
| Critical-failure flag (kappa) | **0.74** [0.37, 1.00] | **0.62** [0.24, 1.00] | 0.24 [-0.24, 0.71] | **0.00** |
| Items scored differently from her | 2 of 15 | 3 of 15 | 5 of 15 | 9 of 15 |
| Legal accuracy (kappa_w) | 0.75 | 0.58 | 0.47 | 0.10 |
| Jurisdictional grounding (kappa_w) | 0.19 | 0.62 | 0.57 | 0.00 |

The two leading intervals overlap almost entirely; see finding 4 for why they
should not be ranked against each other.

The low-cost judge flagged **none** of the nine items she flagged as critical
failures. The two strongest judges produced **no false positives** against her:
every item either of them flagged, she flagged too; they only missed items. That
is six or seven flags each with none misplaced - suggestive, and nowhere near
enough flags to establish a false-positive rate. For a
release gate that asymmetry is the property worth knowing, and it is invisible in
any aggregate score. On 15 items against a non-expert rater this is exploratory
evidence, not an established effect - see L4 through L8. The jurisdictional-
grounding row shows the fragility directly: the judge that tracks her best on the
flag tracks her worst on that dimension.

**4. The pattern is not an artefact of one vendor - but the ranking within the
strong judges is not real.** Adding a GPT-class judge from a different vendor was
the test of whether findings 2 and 3 were a property of the Claude family. They
were not:

- It agreed with the human at the top of the panel (flag kappa **0.74**, 95% CI
  [0.37, 1.00]), alongside the Opus-class judge (**0.62**, [0.24, 1.00]).
- It agreed with the Opus-class judge (flag kappa **0.55**) more than the two
  Claude judges of different tiers agreed with each other (**0.24**). That is
  consistent with capability mattering more than vendor - but with one model per
  vendor this design **cannot separate a vendor effect from a model effect**, and
  the sentence should not be read as establishing one (L14).
- It was the strictest judge on legal accuracy (mean **0.97**, against 1.43 for
  Opus-class and 2.50 for Haiku-class), and it is the only judge with no family
  relationship to the system under test - so its strictness has no
  self-preference explanation, though a single model cannot rule out that this
  vendor is simply harsher.
- Against the low-cost judge it agrees with almost nothing: weighted kappa 0.04 to
  0.16 on every dimension.

**What this does not show.** The cross-vendor judge is *not* demonstrably better
than the Opus-class judge. The difference is **+0.12 with a 95% CI of
[-0.27, 0.52]** and P(better) = 0.61 - a coin flip. In raw terms one differs from
the human on two items and the other on three: the entire gap is **one item out of
fifteen**. Any write-up that ranks these two judges is reading noise. The
separation the data does support is between the strong judges and the low-cost
one, and that one is large - the Haiku-class judge flagged **none** of the nine
items the human flagged, so its kappa of 0.00 is not chance-level agreement but a
rater that never fired at all.

**5. Agreement is worst on the two things a legal product most needs.** Even
between the two strong model judges, the critical-failure flag reached kappa
**0.24** and authority hygiene - the dimension that catches fabricated citations
- reached weighted kappa **0.31**, the lowest of the five.

**6. A substantial share of the agreement was the answer key, not the law.** Removing
the gold reference from the Opus judge's prompt dropped its agreement with its own
gold-reference-equipped self from a 0.86-1.00 ceiling to **0.46-0.75**. The
collapse is worst on authority hygiene: **1.00 to 0.46**. That is the expected
place for it - without a list of expected authorities, "should a citation have
been here?" becomes a judgment call rather than a lookup - and it is direct
evidence for proposal P4, which makes that dimension conditional on an authored
`citation_expected` flag. The flag itself held up better (kappa 0.64, and 19
flags against 18), and the no-gold judge still agreed with the human better than
the Sonnet judge did with the answer key in hand (0.47 vs 0.24).

**7. The failure mode is instrument design, not legal reading.** On most items
where a stricter judge flagged and a lenient one did not, the lenient judge's own
rationale had already named the defect - "Misstates vehicle as Rule 12(e) when
correct answer is Rule 12(c)", "Fails to address DGCL 251(h)... major omission" -
and then did not set the flag. Replacing the holistic flag with four independent
binary checks is proposal P1. Without mandatory rationales this would have been
invisible: kappa alone says "the raters disagree" and implies the raters are the
problem.

**8. Kappa alone would have produced the wrong diagnosis on jurisdiction.** `G1`
vs `G3` showed **100% agreement within one point** on jurisdictional grounding
with weighted kappa of **0.09** and Gwet's AC2 of **0.89** - the kappa paradox,
traceable to a single line of the rubric (adjudication rule 3) that one judge
applied and the other did not. Gwet's coefficient is in the report for exactly
this reason.

**9. The rubric detects the manipulation, with one honest anomaly.** All judges
scored `B_terse` lower on issue completeness and scope discipline. But two scored
it *higher* on legal accuracy (+0.25). The likely explanation is mechanical: a
32-word answer makes fewer legal propositions than a 117-word one, so it has less
surface on which to be wrong. That is a defect in how D1 is defined, and the
second motivation for splitting D1 into conclusion and reasoning (P2).

## Limitations

Sixteen, in the order they most constrain what these results can be used for.
An evaluation write-up that does not list them is not finished.

**On the design of the study**

- **L1 - the pilot pass was not independent, and is on the record rather than
  deleted.** `G1` ran in the context that authored the items, so it knew what each
  trap was designed to catch. It was superseded by independent API passes (one
  call per item, fresh context), is excluded from every headline statistic, and is
  marked non-independent in the rater manifest.
- **L2 - `G3` shares a model family with the system under test**, so its leniency
  is confounded with self-preference. The size of that effect is not separable
  from the capability difference with the data collected here.
- **L3 - sampling stability was measured; prompt stability was not.** The judge
  models reject the `temperature` parameter, so runs are not bit-reproducible.
  The test-retest arm (finding 1) measures that variance directly and finds it
  small - but re-running the *same* prompt tests the smaller risk. Sensitivity to
  how the rubric is worded and ordered is the larger one for an LLM judge and is
  untested here.

**On the human pass**

- **L4 - the human rater is a non-expert.** She validates that the rubric is
  applicable and consistently interpretable against a written gold reference. She
  does **not** validate that the gold references state the law correctly. Nothing
  in her pass establishes legal ground truth.
- **L5 - the human pass was partly contaminated by the interviewer.** Items were
  presented one at a time, each with a short glossary of terms. On at least three
  of the fifteen (PRV-02, COR-05, CON-06) that glossary stated a fact that was
  itself scoring-relevant - that CCPA is an opt-out regime, that the 280G
  cleansing vote is available only to private companies, that a reverse triangular
  merger leaves the target surviving - and the rater's written rationale then
  turned on exactly that point. This inflates her apparent agreement with the
  judges that had the gold reference in front of them. The fix for a future pass
  is a fixed glossary written before any item is shown, containing no proposition
  that appears in a gold reference.
- **L6 - three of her five dimensions carry almost no variance, which makes some
  per-dimension coefficients meaningless rather than impressive.** Two examples
  from the same comparison, the human against the cross-vendor judge: issue
  completeness reads **1.00** because both raters put 14 of 15 items at the same
  single value, and authority hygiene reads **-0.08** because she used two
  categories where the judge used four (Gwet's AC2 on those same cells is 1.00 and
  0.86). Neither number should be quoted as evidence of anything. Her anchoring
  value rests on legal accuracy, jurisdictional grounding and the flag. She scored issue
  completeness 1 on 14 of 15 items, authority hygiene 1 on 13 of 15, and scope
  discipline 1 on 13 of 15. Kappa against a near-constant rater is close to
  uninformative, and where it came out high it is because the other rater is also
  near-constant. Her anchoring value rests on D1, D2 and the flag.
- **L7 - no intra-rater check for the human.** Test-retest is finding 1 for the
  model judges and was not run for her: fifteen items in one sitting, no repeated
  items at the end, no calibration break. Her earlier ratings use more of the
  scale than her later ones, and drift cannot be separated from signal.
- **L8 - the human pass covers 15 of 40 items, and the subset is not a simple
  random sample.** Fourteen items were drawn one per practice-area x
  prompt-condition stratum; the fifteenth was chosen purposively as the item with
  the widest spread across the model judges, which tilts the comparison set
  slightly toward contentious items. At n=15 the interval on a flag kappa spans
  roughly 0.5, which is wide enough that the panel can be split into strong and
  weak but not ordered within those groups.

**On the statistics**

- **L9 - n = 40 (15 for the human), and roughly forty pairwise coefficients are
  reported with no multiplicity control.** Bootstrap CIs on weighted kappa run
  about +/-0.2 at n=40 and wider at n=15. Directions are stable across resamples;
  the precise ranking of dimensions is not. Every comparison in this study should
  be read as exploratory.
- **L10 - items are authored, not sampled.** Every item is built around a trap, so
  the observed critical-failure rates say nothing about the rate a production
  system would show on real traffic. This is a stress test, not a survey.
- **L11 - the ablation removed three components at once.** Dropping the gold
  reference dropped the must-include list, the trap and the expected authorities
  together, so finding 6 cannot attribute the loss to any one of them. The
  authority-hygiene collapse is most plausibly the authorities list specifically -
  testable by removing one component at a time, and not tested.
- **L12 - the flag and D4 are not independent by construction.** The rubric makes
  D4 = 0 set the critical-failure flag automatically, and proposal P1's first
  binary check is that same condition. Any correlation between them is partly
  definitional and is not convergent evidence.
- **L13 - `G1` and `G4` are the same model.** Their pairwise row reads like a
  between-rater comparison and is closer to a retest of one model from a
  contaminated context.

**On coverage**

- **L14 - two vendors, not many.** One cross-vendor judge (`G5`) has been run and
  it replicates the pattern, but the panel is still one vendor on each side, one
  model per vendor, and a system under test from one of them. A third vendor, a
  second model per vendor, or a non-Claude system under test would each test
  something this design cannot.
- **L15 - the prompt-condition manipulation is confounded.** `B_terse` changes
  length, hedging and directness at once, so an effect cannot be attributed to one
  of them. The mechanical explanation offered for the D1 anomaly in finding 9 is a
  hypothesis, not a tested result.
- **L16 - the gold references have not been reviewed by a licensed attorney.**
  They are researched against named primary authority and re-checked against
  primary sources in September 2026 (`docs/verification.md`), but in a production
  programme they would be adjudicated by subject-matter experts before any score
  derived from them was relied on. Several items are deliberately built on rules
  that change - HSR thresholds, FLSA salary levels, EU AI Act application dates -
  and reward an answer that flags the volatility rather than one that states a
  figure.

### The question this study cannot answer

*How do you know the stricter judge is right rather than merely stricter?*

It does not. Agreement is not accuracy. The human pass tests whether the rubric
can be applied consistently against a written gold reference; it does not test
whether the gold reference is correct, and the rater is not a lawyer. Answering
the accuracy question needs adjudicated gold references from practising counsel,
and that is the first thing this study would buy with a budget.

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
