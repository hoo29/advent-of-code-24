from pathlib import Path
from collections import defaultdict


def do1(data: list[str]):
    visited: set[str] = set()
    regions: list[set[str]] = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if f"{x},{y}" in visited:
                continue

            cur_region = set()
            check = [[x, y]]
            char = data[y][x]
            while check:
                cur_pos = check.pop()
                if (cur_pos[0] < 0 or cur_pos[0] >= len(data[0])
                    or cur_pos[1] < 0 or cur_pos[1] >= len(data)
                        or data[cur_pos[1]][cur_pos[0]] != char):
                    continue

                cur_pos_str = f"{cur_pos[0]},{cur_pos[1]}"
                if cur_pos_str in visited:
                    continue

                cur_region.add(cur_pos_str)
                visited.add(cur_pos_str)
                check += [[cur_pos[0], cur_pos[1] - 1], [cur_pos[0] + 1, cur_pos[1]],
                          [cur_pos[0], cur_pos[1] + 1], [cur_pos[0] - 1, cur_pos[1]]]
            regions.append(cur_region)
    sum = 0
    for region in regions:
        per = 0
        for pos in region:
            pos_per = 4
            [x, y] = map(int, pos.split(","))
            for check in [x, y - 1], [x + 1, y], [x, y + 1], [x - 1, y]:
                if f"{check[0]},{check[1]}" in region:
                    pos_per -= 1
            per += pos_per
        sum += (per * len(region))

    print(sum)


def do2(data: list[str]):
    visited: set[str] = set()
    regions: list[set[str]] = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if f"{x},{y}" in visited:
                continue

            cur_region = set()
            check = [[x, y]]
            char = data[y][x]
            while check:
                cur_pos = check.pop()
                if (cur_pos[0] < 0 or cur_pos[0] >= len(data[0])
                    or cur_pos[1] < 0 or cur_pos[1] >= len(data)
                        or data[cur_pos[1]][cur_pos[0]] != char):
                    continue

                cur_pos_str = f"{cur_pos[0]},{cur_pos[1]}"
                if cur_pos_str in visited:
                    continue

                cur_region.add(cur_pos_str)
                visited.add(cur_pos_str)
                check += [[cur_pos[0], cur_pos[1] - 1], [cur_pos[0] + 1, cur_pos[1]],
                          [cur_pos[0], cur_pos[1] + 1], [cur_pos[0] - 1, cur_pos[1]]]
            regions.append(cur_region)
    sum = 0

    for region in regions:
        top: dict[int, list[int]] = defaultdict(list)
        right: dict[int, list[int]] = defaultdict(list)
        bottom: dict[int, list[int]] = defaultdict(list)
        left: dict[int, list[int]] = defaultdict(list)
        for pos in region:
            [x, y] = map(int, pos.split(","))
            for ind, check in enumerate([[x, y - 1], [x + 1, y], [x, y + 1], [x - 1, y]]):
                if f"{check[0]},{check[1]}" in region:
                    continue
                if ind == 0:
                    top[check[1]].append(check[0])
                elif ind == 1:
                    right[check[0]].append(check[1])
                elif ind == 2:
                    bottom[check[1]].append(check[0])
                else:
                    left[check[0]].append(check[1])
        sides = 0
        for edge in [top, right, bottom, left]:
            for _, v in edge.items():
                v.sort()
                cur_sides = 1
                for i in range(len(v) - 1):
                    if v[i + 1] != v[i] + 1:
                        cur_sides += 1
                sides += cur_sides

        sum += (sides * len(region))

    print(sum)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
