from collections import defaultdict
from pathlib import Path


def do1(data: list[str]):
    data = [list(y) for y in data]
    city: dict[str, list[tuple[int]]] = defaultdict(list)
    for y, _ in enumerate(data):
        for x, _ in enumerate(data[y]):
            if data[y][x] != ".":
                city[data[y][x]].append((x, y))

    count = 0
    # for all x y
    for y, _ in enumerate(data):
        for x, _ in enumerate(data[y]):
            print((len(data) * len(data[0])) - (y * len(data[0]) + x))
            for _, locs in city.items():
                if len(locs) == 1:
                    continue
                # calculate dist to each antenna
                dists = [(l[0] - x, l[1] - y)
                         for l in locs if l[0] != x or l[1] != y]
                # check if any are x2 the value of another
                for dist_idx, dist in enumerate(dists):
                    other_dists = dists[:dist_idx] + dists[dist_idx + 1:]
                    antinode = any([l[0] == (dist[0] * 2) and l[1] == (dist[1] * 2)
                                    for l in other_dists])
                    if antinode and data[y][x] != "#":
                        data[y][x] = "#"
                        count += 1

    print()
    for l in data:
        print("".join(l))

    print()
    print(count)


def do2(data: list[str]):
    data = [list(y) for y in data]
    city: dict[str, list[tuple[int]]] = defaultdict(list)
    for y, _ in enumerate(data):
        for x, _ in enumerate(data[y]):
            if data[y][x] != ".":
                city[data[y][x]].append((x, y))

    count = 0
    for _, locs in city.items():
        if len(locs) == 1:
            continue

        for loc in locs:
            x = loc[0]
            y = loc[1]
            dists = [(l[0] - x, l[1] - y)
                     for l in locs if l[0] != x or l[1] != y]
            for dist_idx, _ in enumerate(dists):
                other_dists = dists[:dist_idx] + dists[dist_idx + 1:]
                for l in other_dists:
                    line_x = x
                    line_y = y
                    # mark all other line points in one dir
                    while line_x < len(data[0]) and line_y < len(data) and line_x >= 0 and line_y >= 0:
                        if data[line_y][line_x] != '#':
                            count += 1
                            data[line_y][line_x] = "#"
                        line_x -= l[0]
                        line_y -= l[1]
                    line_x = x
                    line_y = y
                    # and the other
                    while line_x < len(data[0]) and line_y < len(data) and line_x >= 0 and line_y >= 0:
                        if data[line_y][line_x] != '#':
                            count += 1
                            data[line_y][line_x] = "#"
                        line_x += l[0]
                        line_y += l[1]

    print()
    for l in data:
        print("".join(l))

    print()
    print(count)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    # 931 too low
    # 934
    do2(data)


if __name__ == '__main__':
    wrapper()
