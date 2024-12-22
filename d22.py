from pathlib import Path
import os
import json


def do1(data: list[str]):
    count = 2000
    secrets = [int(x) for x in data]
    for _ in range(count):
        for s in range(len(secrets)):
            val = secrets[s]

            val ^= val * 64
            val %= 16777216

            val ^= val // 32
            val %= 16777216

            val ^= val * 2048
            val %= 16777216

            secrets[s] = val
    ans = sum(secrets)
    print(ans)


def do2(data: list[str], test: bool):
    count = 2000
    ext = "test" if test else ""
    load_existing = os.path.isfile(f"./tmp/d21{ext}_secrets")
    if load_existing:
        with open(f"./tmp/d21{ext}_secrets") as f:
            secrets = json.load(f)
        with open(f"./tmp/d21{ext}_prices") as f:
            prices = json.load(f)
        with open(f"./tmp/d21{ext}_diffs") as f:
            diffs = json.load(f)
    else:
        secrets = [[int(x)] for x in data]
        prices = [[int(x) % 10] for x in data]
        diffs = [[] for _ in range(len(data))]
        for ind in range(count):
            print(f"secret iteration {ind + 1}/{count}")
            for s in range(len(secrets)):
                val = secrets[s][-1]

                val ^= val * 64
                val %= 16777216

                val ^= val // 32
                val %= 16777216

                val ^= val * 2048
                val %= 16777216
                prices[s].append(val % 10)
                secrets[s].append(val)
                if ind == 0:
                    continue
                diffs[s].append(prices[s][ind] - prices[s][ind - 1])
        for s in range(len(secrets)):
            diffs[s].append(prices[s][-1] - prices[s][-2])
        with open(f"./tmp/d21{ext}_secrets", "w", encoding="utf-8") as f:
            json.dump(secrets, f, ensure_ascii=False)
        with open(f"./tmp/d21{ext}_prices", "w", encoding="utf-8") as f:
            json.dump(prices, f, ensure_ascii=False)
        with open(f"./tmp/d21{ext}_diffs", "w", encoding="utf-8") as f:
            json.dump(diffs, f, ensure_ascii=False)
    if load_existing:
        with open(f"./tmp/d21{ext}_all_diffs") as f:
            all_diffs = json.load(f)
    else:
        all_diffs = set()
        for ind, d in enumerate(diffs):
            print(f"calculating diffs {ind + 1}/{len(diffs)}")
            for i in range(len(d)):
                if i + 3 >= len(d):
                    break
                all_diffs.add((d[i], d[i + 1], d[i + 2], d[i + 3]))
        with open(f"./tmp/d21{ext}_all_diffs", "w", encoding="utf-8") as f:
            json.dump(list(all_diffs), f, ensure_ascii=False)
        all_diffs = list(all_diffs)
    max = -1
    max_diffs = ""
    for prog_ind, diff_list in enumerate(all_diffs):
        print(f"finding diff {prog_ind + 1}/{len(all_diffs)}")
        diff_max = 0
        for ind, d in enumerate(diffs):
            for i in range(len(d)):
                if i + 3 >= len(d):
                    break
                if (d[i], d[i + 1], d[i + 2], d[i + 3]) == (diff_list[0], diff_list[1], diff_list[2], diff_list[3]):
                    diff_max += prices[ind][i + 3 + 1]
                    break
        if diff_max > max:
            max = diff_max
            max_diffs = diff_list

    print(max)
    print(max_diffs)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]
    # it slow but works
    do2(data, test)


if __name__ == '__main__':
    wrapper()
