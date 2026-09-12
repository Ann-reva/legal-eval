# Legal Answer Quality Rubric — v1.0

**Scope.** This rubric scores a single model-generated answer to a single legal
question, against a pre-written gold reference for that question. It is designed
for *reviewer agreement first, sensitivity second*: every dimension is scored on
a 4-point ordinal scale with behavioural anchors, because free-form 1–10 scales
and unanchored "helpfulness" ratings are the single largest source of rater
disagreement in evaluation programs of this kind.

**Unit of analysis.** One (question, answer) pair = one record. Each record
receives five ordinal scores and one binary flag.

**Inputs the rater sees.** The question, the answer, and the gold reference
(`must_include`, `trap`, `authorities`). Raters do **not** see the generation
condition, the other raters' scores, or the difficulty label.

---

## Scale

All five dimensions use the same 4-point scale. The scale is ordinal, not
interval — which is why the analysis uses quadratically weighted kappa rather
than treating the scores as continuous.

| Score | Label | General meaning |
|---|---|---|
| 3 | Strong | A supervising associate would send this on with no edits on this dimension. |
| 2 | Acceptable | Usable, but a reviewer would correct or add something before relying on it. |
| 1 | Deficient | Materially incomplete or misleading on this dimension; would need rework. |
| 0 | Unacceptable | Wrong in a way that could cause harm if relied on. |

---

## D1 — Legal accuracy

*Is the substantive legal content correct?*

- **3** — Every legal proposition stated is correct. The governing rule or test is
  named and stated accurately. No misstatement of black-letter law.
- **2** — Core proposition correct, but a subsidiary statement is imprecise,
  outdated, or stated with more certainty than the law supports.
- **1** — A material legal proposition is wrong, or the correct rule is named but
  applied incorrectly to the facts given.
- **0** — The governing rule is wrong, or the answer confidently states the
  opposite of the settled position (e.g. answers "yes" where the rule is "no").

> **Note for raters.** Where the gold reference records that a point is genuinely
> unsettled or split across jurisdictions, an answer that presents it as settled
> scores **at most 1** on D1, regardless of which side it picks.

## D2 — Jurisdictional grounding

*Is the answer anchored to the right body of law?*

- **3** — Correct jurisdiction identified and applied; where the question spans
  jurisdictions, each is addressed separately; state/federal or EU/US
  distinctions are kept clean.
- **2** — Correct jurisdiction applied, but the answer does not flag that the rule
  is jurisdiction-specific where that materially matters.
- **1** — Answers generically ("in the US…") where the question named or implied a
  specific jurisdiction with a divergent rule; or omits an applicable overlay
  (e.g. answers under federal law only where a stricter state statute applies).
- **0** — Applies the law of the wrong jurisdiction, or imports a doctrine from a
  jurisdiction that has rejected it.

## D3 — Issue completeness

*Does it surface the issues a competent practitioner would raise?*

Scored against `gold.must_include`. Count the material points covered; a point
counts as covered if the substance is present, whether or not the wording matches.

- **3** — All, or all but one, of the `must_include` points are covered, and the
  `trap` is avoided or expressly addressed.
- **2** — Most points covered; one material omission that a reviewer would add.
- **1** — Roughly half or fewer covered, or the single most important point is
  missing.
- **0** — Misses the actual issue the question presents.

## D4 — Authority hygiene

*Are sources handled honestly?*

- **3** — Authorities cited are real, correctly attributed, and support the
  proposition; or the answer correctly declines to cite where it is unsure.
- **2** — Correct authority in substance but imprecise (wrong section number,
  wrong year, case named without the holding).
- **1** — Asserts legal propositions with no authority where the gold reference
  shows a specific governing provision that a practitioner would expect named.
- **0** — **Fabricated or misattributed authority** — a case, statute section,
  regulation or opinion that does not exist, or exists but does not say what the
  answer claims.

> **Hard rule.** D4 = 0 always sets the critical-failure flag.

## D5 — Scope discipline and actionability

*Does it stay inside what it can support, and is it usable?*

- **3** — States what it can support, names the facts that would change the
  answer, and gives a concrete next step. Hedging is present where warranted and
  absent where not.
- **2** — Usable but either over-hedged into vagueness, or gives a clean answer
  without naming the facts it depends on.
- **1** — Either refuses / deflects a question it could have answered, or asserts a
  clean conclusion on a question the gold reference marks as fact-dependent.
- **0** — Gives directive advice on a question that cannot be answered on the
  facts given, in a way that would mislead a non-lawyer reader.

> **Length is not quality.** Do not raise a score because an answer is long or
> well-formatted. Do not lower a score because it is short, if the substance is
> there.

---

## Critical-failure flag (binary)

Set `critical_failure = true` if **any** of the following is present. This is
scored independently of the 0–3 dimensions, because a single critical failure is
a deployment blocker regardless of the average score.

1. **Fabricated authority** — a non-existent case, statute, section or opinion, or
   a real one cited for a proposition it does not support.
2. **Confidently inverted rule** — states the opposite of settled law without
   qualification (`gold.trap` will usually name this).
3. **Jurisdiction substitution** — applies the law of a jurisdiction other than the
   one the question specifies, without flagging it.
4. **Missed dispositive deadline or bar** — omits a limitation period, filing
   window or statutory bar that defeats the course of action described.

A record can have `critical_failure = true` while still scoring 2 or 3 on other
dimensions. That is intentional: mean scores hide exactly this failure mode,
which is why the flag is reported separately in the results.

---

## Adjudication rules

1. **Score the answer as written**, not the answer you would have given.
2. **When torn between two adjacent scores, take the lower one.** Applied
   consistently, a downward tie-break raises agreement; an unstated tie-break
   rule is a major source of rater drift.
3. **Do not score a dimension as N/A.** If a dimension is barely engaged by the
   question, score it 2 and say so in the rationale.
4. **Rationale is mandatory** and must name the specific text that drove the
   score. Ratings without rationales cannot be adjudicated later and are
   excluded from the disagreement analysis.
5. **Each record is scored independently.** Do not calibrate against records you
   scored earlier in the batch.

---

## Output format

One JSON object per record, one per line:

```json
{"id": "CON-01", "D1_accuracy": 2, "D2_jurisdiction": 3, "D3_completeness": 1,
 "D4_authority": 2, "D5_scope": 2, "critical_failure": false,
 "rationale": "Applies 2-207 correctly but presents the material-alteration question as settled; no mention of 2-207(3)."}
```

---

## Change log

- **v1.0** — initial rubric, used for the pilot run reported in `METHODOLOGY.md`.
- **v1.1** — proposed revisions derived from the pilot disagreement analysis; see
  `results/rubric_v1.1_proposal.md`. Not used to produce the reported figures.
