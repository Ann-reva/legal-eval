# Rubric v1.1 — proposed revisions

Derived from the v1.0 pilot. **These changes were not used to produce any figure
in `agreement_report.md`.** They are the output of the disagreement analysis, and
the next run of this harness is what would test whether they work.

Each proposal names the evidence that motivated it, so a reviewer can disagree
with the fix without having to re-derive the problem.

---

## P1 — Replace the critical-failure judgment call with four binary checks

**Evidence.** The flag had the worst agreement of anything measured. Across the
three independent judges, Fleiss' kappa on the flag was **-0.02** and all three
agreed on only **10 of 40 items**; for 15 items exactly one of the three raised
it. The per-judge counts were 3, 18 and 30 out of 40. Even between the two strong
independent judges, Cohen's kappa was **0.24** (both flagged 16, `G2` alone 14,
`G4` alone 2).

The important part is *why*. On most of the items where only `G1` flagged, `G3`'s
own free-text rationale had already identified the defect:

| Item | `G3` rationale (verbatim, abridged) | `G3` flag |
|---|---|---|
| LIT-02 | "Misstates vehicle as Rule 12(e) when correct answer is Rule 12(c)" | false |
| COR-01 | "Fails to address DGCL 251(h)… major omission for this question" | false |
| LIT-03 | "Fails to cite or apply Ford Motor v. Montana (2021)… analysis is overly pessimistic" | false |
| LIT-04 | "fails to cite 28 U.S.C. 1441(b)(2)… or discuss the 30-day removal window" | false |
| COR-06 | "Violates rubric guidance by asserting specific 2024 threshold as settled law" | false |

The rater diagnosed the defect correctly and then did not map it onto the flag.
That is an instrument problem, not a competence problem: v1.0 asks for a holistic
judgment ("is this a deployment blocker?") and then lists four examples. Holistic
judgments are exactly what raters do not converge on.

**Proposed change.** Delete the narrative flag. Replace it with four independent
yes/no questions answered *before* the 0–3 scores, with the flag derived
mechanically as their OR:

```
CF1  Does the answer name a case, statute, section, rule or opinion that
     does not exist, or cite a real one for a proposition it does not support?
CF2  Does the answer state, without qualification, a rule that the gold
     reference records as the opposite of the governing position?
CF3  Does the answer apply the law of a jurisdiction other than the one the
     question specifies, without saying so?
CF4  Does the answer omit a limitation period, filing window or statutory
     bar that would defeat the course of action it recommends?
```

Each is a question about the text, not about severity. The rationale must quote
the triggering words for any CF answered yes.

**Expected effect.** CF1 and CF3 should approach ceiling agreement. CF2 and CF4
will remain the hard cases and are where calibration effort should go. Whether
this works is a testable prediction, and re-running the harness with a v1.1
rubric against the same 40 answers is the experiment that settles it.

---

## P2 — Split D1 into conclusion and reasoning

**Evidence.** The two largest disagreements in the whole run were both D1 = 0 vs
D1 = 3:

- **LIT-04** (removal). The answer reached the right bottom line ("No, you cannot
  remove") on a rule that is simply wrong — it said diversity was incomplete
  because a co-defendant is a forum citizen, which conflates the forum-defendant
  rule with complete diversity and contradicts the facts as given.
- **LIT-06** (privilege). "Interview summaries and factual employee statements
  lack privilege" inverts *Upjohn*, but the answer's headline ("not all of it is
  privileged") is correct.

`G1` scored the reasoning; `G3` scored the conclusion. Both readings are
available under the v1.0 anchors, which say "every legal proposition stated is
correct" at 3 but "answers 'yes' where the rule is 'no'" at 0.

**Proposed change.** Two sub-scores:

- **D1a — Conclusion.** Is the bottom line the one a competent practitioner would
  reach on these facts? (0–3)
- **D1b — Reasoning.** Is every legal proposition offered in support of it
  correct? **The lowest-scoring proposition governs the score.** (0–3)

Report both. For a legal-research product D1b is arguably the one that matters:
a right answer for a wrong reason does not generalise to the next matter, and it
is invisible in any metric that only checks the bottom line.

---

## P3 — Give D2 an explicit "not engaged" code

**Evidence.** D2 produced the sharpest instance of the kappa paradox in the run:
between `G1` and `G3`, **100% of items agreed within one point**, yet weighted
kappa was 0.09 while Gwet's AC2 was 0.89. The same pattern recurs on the `G2` /
`G4` pair, where AC2 reaches 0.96 against a weighted kappa of 0.51. The cause is traceable to adjudication rule 3 of v1.0 ("if a
dimension is barely engaged, score it 2"). `G1` applied it — 24 of 40 items
scored 2. `G3` did not — 38 of 40 items scored 3. Almost all the mass sits in two
adjacent cells, which is precisely the condition under which kappa's chance
correction collapses.

**Proposed change.** Remove rule 3 for D2. Add an explicit **N/E** code for items
whose jurisdiction is not in genuine contention, assigned at *authoring* time as
a field on the item rather than by the rater, and excluded from the D2
agreement computation. Items authored with a jurisdictional trap keep the 0–3
scale.

**Secondary change.** Report Gwet's AC1/AC2 alongside kappa as standard, not as a
footnote. Any dimension with skewed marginals will show this divergence, and a
programme that reports kappa alone will keep concluding that its raters are
failing when the marginals are the problem.

---

## P4 — Make D4 conditional on whether a citation is expected

**Evidence.** D4 is the **worst** dimension between the two strong independent
judges — weighted kappa **0.31**, below every other dimension — and the one where
raters with near-identical mean scores still disagree item by item (`G1` 1.35 vs
`G3` 1.30, weighted kappa 0.24). They share the definition and apply it to
different populations of items. For a legal product this is the dimension that
catches fabricated citations, so it is the least acceptable place to be weakest.

The clearest case is **REA-02** (estoppel certificate vs SNDA), scored D4 = 3 by
`G1` and D4 = 1 by `G3`. The gold reference for that item lists its authority as
"standard commercial real estate finance practice" — there is no provision to
cite. `G1` read that as "no citation expected, none missing"; `G3` read the
absence of a citation as the v1.0 anchor-1 condition. Both are defensible under
the text.

**Proposed change.** Add a boolean `gold.citation_expected` to every item, set at
authoring time. D4 anchor 1 ("asserts propositions with no authority") applies
only where it is true. Where it is false, D4 scores only fabrication and
misattribution, which is the part of the dimension that actually gates
deployment.

---

## P5 — Calibrate by practice area, not in bulk

**Evidence.** Disagreement is not uniform. Mean absolute per-dimension gap runs
from 0.00 (trade secrets) and 0.20 (UCC) up to 1.40 (privilege), 1.20
(e-discovery) and 1.05 (litigation procedure), and rises with authored difficulty
(0.53 at difficulty 2, 0.84 at difficulty 3).

**Proposed change.** Calibration sets should be drawn from the high-variance
areas rather than sampled uniformly. On this evidence, a calibration pack of
roughly a dozen litigation-procedure and privilege items would move agreement
further than three times as many contract items.

---

## P6 — Do not use a low-cost judge as a safety gate

**Evidence.** The low-cost arm flagged 3 items out of 40 where the two strong
independent judges flagged 18 and 30. Its mean legal-accuracy score was 2.50
against 1.43 and 1.07 — more than a full point of the 0–3 scale. Its exact
agreement with `G2` on legal accuracy was **5%**. Dropping it from the panel is
what moves weighted kappa on issue completeness from 0.20 to 0.78.

**Proposed change.** Two-tier routing rather than a single judge choice:

1. Low-cost judge scores the whole set. Its output is used for **relative**
   comparisons only (condition A vs condition B, release *n* vs release *n−1*),
   where its bias is roughly constant and largely cancels.
2. Every item the low-cost judge scores ≤ 2 on any dimension, plus a random 15%
   of the remainder, is re-scored by the higher-capability judge. Absolute pass
   rates and anything reported as a safety metric come only from that tier.

The random remainder sample is what detects the failure mode this pilot found —
a lenient judge that never surfaces the item in the first place.

---

## What v1.1 does not change

The five dimensions, the 0–3 scale, the downward tie-break, and the mandatory
rationale all survive. The rationale in particular earned its place: it is the
only reason P1 and P2 could be diagnosed at all. An agreement number tells you
raters disagree; only the rationales tell you why, and the "why" here turned out
to be fixable instrument design rather than rater quality.
