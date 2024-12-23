from pathlib import Path
from collections import defaultdict
from itertools import combinations


def do1(data: list[str]):
    cons = defaultdict(list[str])
    for l in data:
        parts = l.split("-")
        cons[parts[0]].append(parts[1])
        cons[parts[1]].append(parts[0])

    sets = []
    ans = 0
    seen = set()
    for k, v in cons.items():
        for p in combinations(v, 2):
            combo = [k, p[0], p[1]]
            key = str(sorted(combo))
            if key in seen:
                continue
            if k in cons[p[0]] and p[1] in cons[p[0]]:
                sets.append(combo)
                if any(x.startswith("t") for x in combo):
                    ans += 1
            seen.add(key)
    print(ans)


def do2(data: list[str]):
    cons = defaultdict(list[str])
    for l in data:
        parts = l.split("-")
        cons[parts[0]].append(parts[1])
        cons[parts[1]].append(parts[0])

    sets = []
    seen = set()
    max_len = -1
    max_ans = []
    for k, v in cons.items():
        for ind in range(2,  len(v)):
            for p in combinations(v, ind):
                combo = [k, *p]
                key = str(sorted(combo))
                if key in seen:
                    continue
                connected = True
                for sub_combo in combinations(combo, 2):
                    if sub_combo[0] not in cons[sub_combo[1]] or sub_combo[1] not in cons[sub_combo[0]]:
                        connected = False
                        break
                if connected:
                    sets.append(combo)
                    if len(combo) > max_len:
                        max_len = len(combo)
                        max_ans = combo
                seen.add(key)
    max_ans.sort()
    print(",".join(max_ans))


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
