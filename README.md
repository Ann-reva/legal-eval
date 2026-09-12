# legal-eval — inter-rater agreement for LLM judges on legal answers

A complete, reproducible evaluation study in one small repository: 40 legal
questions with gold references, a written rubric, a system under test run under
two prompt conditions, two independent model judges, and the inter-rater
statistics that say whether the judges are measuring the same thing.

**Headline result.** Judges applying the same rubric to the same 40 answers
flagged between **8% and 75%** of them as release blockers. That divergence is not
noise: re-running each judge on the same items reproduced its own scores at
weighted kappa **0.86-1.00** (the Opus-class judge reproduced all 18 of its flags
exactly), while agreement *between* judges ran 0.09-0.78. The disagreement is a
stable property of the judge, not run-to-run variance.

A human rater scored 15 of the items to anchor it. Her average severity is
identical to the Sonnet-class judge - and item by item she agrees far more with
the Opus-class judge (flag kappa **0.62** vs **0.24**). The low-cost judge caught
**zero of the nine** items she flagged as critical failures. **Matching a judge to
a human by average score picks the wrong judge.**

Removing the gold reference from a judge's prompt cost roughly a third of its
agreement with itself - and almost all of it on authority hygiene (1.00 to 0.46).
Much of what looked like legal judgment was checklist matching.

The full argument is in **[`METHODOLOGY.md`](METHODOLOGY.md)** (two pages).

![Same judge vs other judges vs the human rater](results/figures/intra_vs_inter.png)
![Rater severity](results/figures/rater_severity.png)
![Critical-failure spread](results/figures/critical_failure_spread.png)
![Agreement by dimension](results/figures/agreement_by_dimension.png)

## What is here

```
data/
  questions.jsonl              40 items: practice area, jurisdiction, difficulty,
                               failure-mode probe, and a gold reference
                               (must_include / trap / authorities)
  answers.jsonl                40 answers from the system under test, tagged with
                               the prompt condition that produced them
  grades/G1..G4.jsonl          per-item ratings from each model judge, with rationales
  grades/GH.jsonl              human rater, 15 items (non-expert, rubric-trained)
  grades/G2b, G4b.jsonl        test-retest arms: same judge, same prompt, second run
  grades/G4ng.jsonl            ablation arm: same judge, gold reference withheld
  _human_sample.json           which items the human pass covered, and why
  grades/raters.json           rater manifest: model, execution, independence
docs/
  rubric.md                    the rubric, v1.0 — five 0-3 dimensions, anchors,
                               critical-failure definitions, adjudication rules
  run_log.md                   what was actually run, and what the API would not
                               let the harness control
  verification.md              what was checked and how — statistics validated
                               against reference implementations, legal claims
                               re-checked against primary sources
  grader_prompts/              the exact prompts used, for both the system under
                               test and the judges
src/
  agreement.py                 Cohen / Fleiss / Krippendorff / Gwet, from scratch
  analyze.py                   builds the report, the CSV, the disagreement dossier
  figures.py                   the two figures above
  run_graders.py               run a judge via API — Anthropic / OpenAI / Google
  human_sheet.py               make and ingest a human rating pass
  sample_human_items.py        reproducible stratified sampling for that pass
tests/
  test_agreement.py            every estimator vs published worked examples and
                               vs scikit-learn and the krippendorff package
results/
  agreement_report.md          the numbers
  disagreements.md             every split, with both rationales side by side
  rubric_v1.1_proposal.md      six proposed fixes, each tied to its evidence
  scores_long.csv              tidy long-format scores for your own analysis
```

## Reproduce

```bash
pip install -r requirements.txt
python tests/test_agreement.py     # validate the statistics first
python src/analyze.py              # rebuild results/ from data/grades/
python src/figures.py
```

`make all` does the same.

## Extend

**Add a cross-vendor judge.** All four judges here are Claude models, which is
limitation L6. An OpenAI or Google judge is the most informative addition.

```bash
export ANTHROPIC_API_KEY=...
python src/run_graders.py --provider anthropic --model claude-sonnet-4-5 --out G2

export OPENAI_API_KEY=...
python src/run_graders.py --provider openai --model gpt-4.1 --out G4

python src/analyze.py      # Fleiss' kappa and Krippendorff's alpha appear at 3+ raters
```

One independent API call per item, temperature 0, randomised presentation order
per judge. The rater is registered in `raters.json` automatically.

**Add more human ratings.** Fifteen items are enough to rank the judges and not
enough to be precise about any one dimension. The sheet below extends the pass;
Krippendorff's alpha handles the partial coverage.

```bash
python src/human_sheet.py --make                 # -> results/human_rating_sheet.csv
# fill the six score columns in a spreadsheet, save as CSV
python src/human_sheet.py --ingest results/human_rating_sheet.csv --out GH
python src/analyze.py
```

A partial pass is fine — score 15 of the 40 and leave the rest blank.
Krippendorff's alpha handles the missing cells, which is why it is the right
headline statistic once humans are in the panel.

**Swap in your own items.** Everything downstream keys off
`data/questions.jsonl`. Keep the `gold` block shape — `must_include`, `trap`,
`authorities` — and the rubric, harness, statistics and report all work
unchanged.

## Reading the numbers honestly

- **n = 40.** Bootstrap CIs on weighted kappa run roughly ±0.2. Directions are
  stable; point estimates are not precise.
- **Landis–Koch labels** ("fair", "moderate") are a 1977 rule of thumb reported
  for orientation, not a decision rule.
- **Kappa and Gwet's AC are both reported** because they disagree sharply on two
  dimensions here, and the disagreement is diagnostic rather than noise — see
  finding 4 in `METHODOLOGY.md`.
- **The gold references were authored for this study and have not been reviewed
  by a licensed attorney.** See limitation L7.
- **Sampling is not pinned**, but its effect is measured: the test-retest arm puts
  intra-rater agreement at 0.86-1.00. See L3.
- **The human rater is a non-expert** applying the rubric against a written gold
  reference. She does not validate that the gold references state the law
  correctly. See L4.

Nothing in this repository is legal advice.

## Licence

MIT for the code. The question set, gold references and rubric are released under
CC BY 4.0.
