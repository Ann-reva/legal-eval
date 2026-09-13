# Run log

## Rating passes

| Rater | Model | How | Items | Date |
|---|---|---|---|---|
| `G1` | claude-opus-5 | main session, all 40 items in one context | 40/40 | 2026-09-11 |
| `G3` | claude-haiku | cold subagent, fresh context | 40/40 | 2026-09-11 |
| `G2` | claude-sonnet-5 | API via `src/run_graders.py`, one call per item | 40/40 | 2026-09-12 |
| `G4` | claude-opus-5 | API via `src/run_graders.py`, one call per item | 40/40 | 2026-09-12 |
| `GH` | human (non-expert, rubric-trained) | manual, one item at a time, no other rater's scores shown | 15/40 | 2026-09-12 |
| `G4b` | claude-opus-5 | test-retest: same prompt, different order, second run | 40/40 | 2026-09-12 |
| `G2b` | claude-sonnet-5 | test-retest: same prompt, different order, second run | 40/40 | 2026-09-12 |
| `G4ng` | claude-opus-5 | ablation: gold reference withheld from the prompt | 39/40 | 2026-09-12 |
| `G5` | gpt-6-astra (different vendor) | API, one independent call per item | 40/40 | 2026-09-13 |

## Notes from the API runs

**Sampling could not be pinned.** Both `claude-sonnet-5` and `claude-opus-5`
reject the `temperature` parameter — the API returns
`temperature is deprecated for this model`. The runs therefore used each model's
default sampling. `run_graders.py` probes the accepted request shape once,
caches it, and prints a notice when temperature is unavailable. Consequence: the
runs are **not bit-reproducible**. Recorded as limitation L3 rather than hidden;
a programme that needs reproducible judging has to pick models that still expose
sampling controls, or accept and measure the run-to-run variance.

**Extended thinking was disabled.** Both models default to extended thinking,
which consumed the entire output budget before any JSON was emitted (first
attempt: `stop_reason: max_tokens`, 700 of 700 tokens spent on thinking, empty
text block). The runs pass `thinking={"type": "disabled"}`. This is a judging
configuration choice and should be stated: a judge allowed to reason at length
may behave differently, and comparing thinking and non-thinking judges is a
sensible follow-up experiment.

**One item failed in the ablation arm** (`G4ng`, 39/40) after three retries. It is
left missing rather than backfilled by hand; the analysis computes every
comparison on the items the two raters actually share and prints the n.

**Human pass.** The 15 items were selected by `src/sample_human_items.py`
(seed 2026) *before* any human rating was collected: one item drawn at random from
each of the 14 practice-area x prompt-condition strata, plus the single item with
the widest spread across the three independent model judges. The rater saw the
question, the gold reference and the answer, one item at a time, and no model
scores at any point.

**Cross-vendor pass provenance.** `G5` was run in two parts. 38 items completed in
the main pass at the default presentation-order seed (50110, crc32 of the rater
id). Two items failed against a new-account rate limit of 10k tokens/minute with
four concurrent workers, and were re-run sequentially with a pause at seed 785.
Recorded here rather than smoothed over: the split does not affect the ratings,
but a reader reconstructing the run needs both seeds. The practical lesson is that
`--workers 4` is too aggressive for a fresh API account.

**Cost.** Roughly 132k input and 12k output tokens per 40-item pass; nine passes
in total, across two vendors.

## Rebuilding

```bash
python3 tests/test_agreement.py
python3 src/analyze.py
python3 src/figures.py
```

`results/` is regenerated entirely from `data/`; nothing in it is hand-edited.
