# Run log

## Rating passes

| Rater | Model | How | Items | Date |
|---|---|---|---|---|
| `G1` | claude-opus-5 | main session, all 40 items in one context | 40/40 | 2026-09-11 |
| `G3` | claude-haiku | cold subagent, fresh context | 40/40 | 2026-09-11 |
| `G2` | claude-sonnet-5 | API via `src/run_graders.py`, one call per item | 40/40 | 2026-09-12 |
| `G4` | claude-opus-5 | API via `src/run_graders.py`, one call per item | 40/40 | 2026-09-12 |

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

**Cost.** Roughly 132k input and 12k output tokens per 40-item pass.

## Rebuilding

```bash
python3 tests/test_agreement.py
python3 src/analyze.py
python3 src/figures.py
```

`results/` is regenerated entirely from `data/`; nothing in it is hand-edited.
