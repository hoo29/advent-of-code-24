from pathlib import Path


def do1(data: list[str]):
    locks: list[set[tuple]] = []
    keys: list[set[tuple]] = []
    for ind in range(0, len(data), 8):
        item = data[ind: ind + 7]
        points = set()
        for y in range(len(item)):
            for x in range(len(item[0])):
                if item[y][x] == "#":
                    points.add((x, y))
        if item[0] == "#####":
            locks.append(points)
        else:
            keys.append(points)
    ans = 0
    for l in locks:
        for k in keys:
            if not l.intersection(k):
                ans += 1
    print(ans)


def do2(data: list[str]):
    print("done")


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do1(data)


if __name__ == '__main__':
    wrapper()
