#!/usr/bin/env python3
"""Run a model judge over the item set via API, one independent call per item.

Why one call per item: a judge that scores 40 items inside a single context is
calibrating against its own earlier scores, which inflates agreement with itself
and deflates it with everyone else. Each item here gets a fresh request at
temperature 0, in a randomised order that differs per judge.

Usage
-----
    export ANTHROPIC_API_KEY=...        # or OPENAI_API_KEY / GOOGLE_API_KEY
    python src/run_graders.py --provider anthropic --model claude-sonnet-4-5 --out G2
    python src/run_graders.py --provider openai    --model gpt-4.1          --out G4

Then re-run `python src/analyze.py` - the new rater is picked up automatically
once it has an entry in data/grades/raters.json.
"""
from __future__ import annotations
import argparse, json, os, random, sys, time, zlib
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIMS = ["D1_accuracy", "D2_jurisdiction", "D3_completeness", "D4_authority", "D5_scope"]

SYSTEM = """You are an independent rater in an evaluation study. Apply the rubric below \
exactly as written, including the tie-break rule and the critical-failure definitions. \
Score the answer as written, not the answer you would have given. Use the full range of \
the scale. Reply with a single JSON object and nothing else.

--- RUBRIC ---
{rubric}
--- END RUBRIC ---"""

USER = """QUESTION ({jurisdiction})
{question}

GOLD REFERENCE
Must include:
{must}
Trap: {trap}
Authorities a practitioner would expect: {auth}

ANSWER UNDER TEST
{answer}

Return JSON with exactly these keys: D1_accuracy, D2_jurisdiction, D3_completeness, \
D4_authority, D5_scope (each an integer 0-3), critical_failure (boolean), and rationale \
(one or two sentences naming the specific text that drove the scores)."""


USER_NO_GOLD = """QUESTION ({jurisdiction})
{question}

ANSWER UNDER TEST
{answer}

No gold reference is provided for this item. Judge it on your own knowledge of the law.

Return JSON with exactly these keys: D1_accuracy, D2_jurisdiction, D3_completeness, \
D4_authority, D5_scope (each an integer 0-3), critical_failure (boolean), and rationale \
(one or two sentences naming the specific text that drove the scores)."""


def build_prompt(rec, rubric, no_gold=False):
    """The no_gold variant removes the answer key.

    With the gold reference in the prompt, the task is partly 'match the checklist'.
    Running one judge without it measures how much of the agreement was the answer
    key doing the work rather than the model's own legal knowledge - see the
    no-gold arm in METHODOLOGY.md.
    """
    if no_gold:
        return (SYSTEM.format(rubric=rubric),
                USER_NO_GOLD.format(jurisdiction=rec["jurisdiction"],
                                    question=rec["question"], answer=rec["answer"]))
    must = "\n".join(f"- {m}" for m in rec["gold_reference"]["must_include"])
    return (SYSTEM.format(rubric=rubric),
            USER.format(jurisdiction=rec["jurisdiction"], question=rec["question"],
                        must=must, trap=rec["gold_reference"]["trap"],
                        auth="; ".join(rec["gold_reference"]["authorities"]),
                        answer=rec["answer"]))


# --------------------------------------------------------------------------- #
# providers
# --------------------------------------------------------------------------- #

_ANTHROPIC_SAMPLING = None   # cached: which sampling-parameter shape this model accepts


def call_anthropic(model, system, user):
    """Send one judging request.

    Sampling control has moved around across SDK and model generations, and some
    current models reject `temperature` outright ("deprecated for this model").
    Probe once, cache the shape that works, and record in the run log when
    temperature could not be pinned - that is a fact the write-up has to state
    rather than a detail to paper over.
    """
    import anthropic
    global _ANTHROPIC_SAMPLING
    c = anthropic.Anthropic()
    base = dict(model=model, max_tokens=1000, system=system,
                messages=[{"role": "user", "content": user}])
    shapes = ([_ANTHROPIC_SAMPLING] if _ANTHROPIC_SAMPLING is not None
              else [{"thinking": {"type": "disabled"}, "temperature": 0},
                    {"thinking": {"type": "disabled"}},
                    {"temperature": 0},
                    {}])
    last = None
    for kw in shapes:
        try:
            r = c.messages.create(**base, **kw)
        except (TypeError, anthropic.BadRequestError) as e:
            last = e
            continue
        if _ANTHROPIC_SAMPLING is None:
            _ANTHROPIC_SAMPLING = kw
            if "temperature" not in kw:
                print("  note: this model rejects `temperature`; running at its "
                      "default sampling. Recorded in the run log.", file=sys.stderr)
        return "".join(b.text for b in r.content if getattr(b, "type", "") == "text")
    raise RuntimeError(f"no accepted request shape for {model}: {last}")


_OPENAI_SHAPE = None


def call_openai(model, system, user):
    """Send one judging request to OpenAI.

    Newer models reject `temperature` and some reject `response_format`, exactly
    as the Anthropic models in this study reject `temperature`. Probe the shapes
    once, cache what works, and say so rather than failing 40 times.
    """
    from openai import OpenAI, BadRequestError
    global _OPENAI_SHAPE
    c = OpenAI()
    base = dict(model=model,
                messages=[{"role": "system", "content": system},
                          {"role": "user", "content": user}])
    shapes = ([_OPENAI_SHAPE] if _OPENAI_SHAPE is not None else [
        {"temperature": 0, "response_format": {"type": "json_object"}},
        {"response_format": {"type": "json_object"}},
        {"temperature": 0},
        {},
    ])
    last = None
    for kw in shapes:
        try:
            r = c.chat.completions.create(**base, **kw)
        except (TypeError, BadRequestError) as e:
            last = e
            continue
        if _OPENAI_SHAPE is None:
            _OPENAI_SHAPE = kw
            if "temperature" not in kw:
                print("  note: this model rejects `temperature`; running at its "
                      "default sampling. Recorded in the run log.", file=sys.stderr)
            if "response_format" not in kw:
                print("  note: this model rejects `response_format`; relying on the "
                      "prompt for JSON.", file=sys.stderr)
        return r.choices[0].message.content


def call_google(model, system, user):
    import google.generativeai as genai
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    m = genai.GenerativeModel(model, system_instruction=system)
    r = m.generate_content(user, generation_config={"temperature": 0,
                                                    "response_mime_type": "application/json"})
    return r.text


PROVIDERS = {"anthropic": call_anthropic, "openai": call_openai, "google": call_google}


def parse(text):
    t = text.strip()
    if t.startswith("```"):
        t = t.split("```")[1].lstrip("json").strip()
    i, j = t.find("{"), t.rfind("}")
    obj = json.loads(t[i:j + 1])
    for d in DIMS:
        v = int(obj[d])
        if v not in (0, 1, 2, 3):
            raise ValueError(f"{d} out of range: {v}")
        obj[d] = v
    obj["critical_failure"] = bool(obj["critical_failure"])
    obj["rationale"] = str(obj.get("rationale", "")).strip()
    if not obj["rationale"]:
        raise ValueError("empty rationale")
    return {k: obj[k] for k in DIMS + ["critical_failure", "rationale"]}


def grade_one(fn, model, rec, rubric, retries=3, no_gold=False):
    system, user = build_prompt(rec, rubric, no_gold)
    last = None
    for a in range(retries):
        try:
            return {"id": rec["id"], **parse(fn(model, system, user))}
        except Exception as e:                      # noqa: BLE001
            last = e
            time.sleep(2 ** a)
    print(f"  ! {rec['id']} failed: {last}", file=sys.stderr)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True, choices=sorted(PROVIDERS))
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", required=True, help="rater id, e.g. G2")
    ap.add_argument("--seed", type=int, default=None,
                    help="presentation-order seed; default is crc32 of --out, which is stable")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--no-gold", action="store_true",
                    help="hide the gold reference from the judge (ablation arm)")
    ap.add_argument("--limit", type=int, default=None,
                    help="grade only the first N items - use --limit 1 as a preflight "
                         "to check the model name and request shape before spending a "
                         "full pass")
    ap.add_argument("--dry-run", action="store_true",
                    help="with --limit, print the parsed rating and write nothing")
    a = ap.parse_args()

    rubric = open(f"{ROOT}/docs/rubric.md").read()
    qs = [json.loads(l) for l in open(f"{ROOT}/data/questions.jsonl")]
    ans = {json.loads(l)["id"]: json.loads(l)["answer"] for l in open(f"{ROOT}/data/answers.jsonl")}
    recs = [{"id": q["id"], "jurisdiction": q["jurisdiction"], "question": q["question"],
             "gold_reference": {k: q["gold"][k] for k in ("must_include", "trap", "authorities")},
             "answer": ans[q["id"]]} for q in qs]
    # Deterministic default: Python's str hash is salted per process (PYTHONHASHSEED),
    # so hash(name) would give a different presentation order on every run and the
    # default invocation would not be reproducible. crc32 is stable across processes,
    # platforms and Python versions.
    seed = a.seed if a.seed is not None else zlib.crc32(a.out.encode()) % 100_000
    print(f"presentation-order seed: {seed}")
    random.Random(seed).shuffle(recs)
    if a.limit:
        recs = recs[:a.limit]

    fn = PROVIDERS[a.provider]
    print(f"grading {len(recs)} items with {a.provider}:{a.model} -> data/grades/{a.out}.jsonl")
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        out = list(ex.map(lambda r: grade_one(fn, a.model, r, rubric, no_gold=a.no_gold), recs))
    out = [o for o in out if o]

    if a.dry_run:
        print(json.dumps(out, indent=2))
        print(f"\ndry run: {len(out)}/{len(recs)} parsed, nothing written. "
              "Drop --dry-run and --limit to run the full pass.")
        return

    path = f"{ROOT}/data/grades/{a.out}.jsonl"
    with open(path, "w") as f:
        for o in out:
            f.write(json.dumps(o) + "\n")
    print(f"wrote {len(out)}/{len(recs)} ratings to {path}")

    # register the rater so analyze.py picks it up
    mpath = f"{ROOT}/data/grades/raters.json"
    meta = json.load(open(mpath))
    meta[a.out] = {"seed": seed, "label": f"{a.provider}:{a.model}" + (" (no gold reference)" if a.no_gold else ""),
                   "model": a.model,
                   "execution": "API, one independent call per item"
                                + (", gold reference withheld" if a.no_gold else ""),
                   "independence": "independent", "role": "model judge",
                   "headline": False}
    json.dump(meta, open(mpath, "w"), indent=2)
    print(f"registered {a.out} in raters.json - now run: python src/analyze.py")


if __name__ == "__main__":
    main()
