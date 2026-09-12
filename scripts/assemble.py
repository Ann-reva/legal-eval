import json, sys, importlib.util, pathlib
items=[]
for p in ["build_questions_part1.py","build_questions_part2.py","build_questions_part3.py"]:
    spec=importlib.util.spec_from_file_location(p[:-3], pathlib.Path("scripts")/p)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    items.extend(m.ITEMS)
ids=[i["id"] for i in items]
assert len(ids)==len(set(ids)), "duplicate ids"
# Deterministic assignment of the answer-generation condition, alternating within
# each practice-area block so conditions are balanced across domain and difficulty.
from collections import defaultdict
c=defaultdict(int)
for it in items:
    k=it["id"][:3]
    it["gen_condition"]= "A_standard" if c[k]%2==0 else "B_terse"
    c[k]+=1
with open("data/questions.jsonl","w") as f:
    for it in items:
        f.write(json.dumps(it, ensure_ascii=False)+"\n")
print("items:",len(items))
import collections
print("by area:", collections.Counter(i["id"][:3] for i in items))
print("by condition:", collections.Counter(i["gen_condition"] for i in items))
print("by difficulty:", collections.Counter(i["difficulty"] for i in items))
