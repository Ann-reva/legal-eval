# legal-eval — inter-rater agreement for LLM judges on legal answers

A complete, reproducible evaluation study in one small repository: 40 legal
questions with gold references, a written rubric, a system under test run under
two prompt conditions, two independent model judges, and the inter-rater
statistics that say whether the judges are measuring the same thing.

**Headline result:** four judges applied the same rubric to the same 40 answers.
The number of answers they flagged as a release blocker ran from **3 to 30**.
Across the three independent judges, Fleiss' kappa was **at or below 0.03 on
every dimension**, and all three agreed about whether an item is a blocker on
only **10 of 40 items**.

The cause is not that the rubric is unusable. Restricted to the two strong
independent judges, weighted kappa reaches 0.78 on issue completeness and 0.72 on
legal accuracy — the low-cost judge is a different instrument, not a noisier copy
of the same one. And where the lenient judges failed to flag, their own written
rationales had usually already named the defect, which makes this a fixable
problem of instrument design rather than of rater capability.

The full argument is in **[`METHODOLOGY.md`](METHODOLOGY.md)** (two pages).

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
  grades/G1..G4.jsonl          per-item ratings from each judge, with rationales
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

**Add a human rating pass.** Given how far apart the judges are, this is now the
most valuable missing piece — it is the only thing that says which judge is
closer to right rather than merely whether two of them agree.

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
- **Sampling is not pinned.** The judge models reject the `temperature`
  parameter, so re-running will not reproduce these exact ratings. See L3.

Nothing in this repository is legal advice.

## Licence

MIT for the code. The question set, gold references and rubric are released under
CC BY 4.0.
