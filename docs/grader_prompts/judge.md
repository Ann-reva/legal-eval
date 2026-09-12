# Judge prompt

Each judge received the complete text of `docs/rubric.md` as its system prompt,
followed by one item at a time. Judges saw the question, its jurisdiction, the
gold reference, and the answer. They did **not** see the generation condition,
the authored difficulty, or any other rater's output, and each judge received the
items in its own randomised presentation order.

## System

> You are an independent rater in an evaluation study. Apply the rubric below
> exactly as written, including the tie-break rule and the critical-failure
> definitions. Score the answer as written, not the answer you would have given.
> Use the full range of the scale. Reply with a single JSON object and nothing
> else.
>
> `--- RUBRIC ---` *(full text of docs/rubric.md)* `--- END RUBRIC ---`

## User (per item)

> QUESTION ({jurisdiction})
> {question}
>
> GOLD REFERENCE
> Must include:
> {must_include, one per line}
> Trap: {trap}
> Authorities a practitioner would expect: {authorities}
>
> ANSWER UNDER TEST
> {answer}
>
> Return JSON with exactly these keys: D1_accuracy, D2_jurisdiction,
> D3_completeness, D4_authority, D5_scope (each an integer 0-3),
> critical_failure (boolean), and rationale (one or two sentences naming the
> specific text that drove the scores).

This is the prompt `src/run_graders.py` sends, verbatim, at temperature 0, one
independent API call per item.
