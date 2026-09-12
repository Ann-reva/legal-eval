# System under test — exact prompts

The 40 answers in `data/answers.jsonl` were produced by a Haiku-class model in a
cold context with no access to the gold references, the rubric, or any other file
in this repository. Twenty items were assigned to each condition
deterministically, alternating within each practice-area block so the conditions
are balanced across domain and difficulty.

## Condition A — `A_standard`

> You are acting as a general-purpose AI legal assistant used by lawyers.
> Answer each legal question helpfully and professionally for a practising
> lawyer. Normal length, roughly 120-200 words each.

Resulting median length: **117 words** (range 105-129).

## Condition B — `B_terse`

> The user is an experienced lawyer who finds hedging annoying. Give a direct
> answer. Do not add disclaimers. Do not say "consult a lawyer". Do not list
> caveats or alternatives unless they are essential. Keep each answer under
> 80 words. Lead with the conclusion.

Resulting median length: **32 words** (range 25-44).

Condition B is not a straw man. It is close to what a product team writes when
users complain that an assistant hedges too much, and the point of including it
is to see whether the rubric can detect the resulting quality change and whether
two judges agree about its size.
