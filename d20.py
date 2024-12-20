from pathlib import Path
import sys

sys.setrecursionlimit(20000)


def get_all_costs(data: list[str], pos: tuple[int], count: int, costs: dict[tuple[int], int], history: set[tuple[int]]):
    history.add(pos)
    costs[pos] = count
    if data[pos[1]][pos[0]] == "S":
        return
    for d in [
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1]),
    ]:
        next_char = data[d[1]][d[0]]
        if next_char in [".", "S"] and d not in history:
            get_all_costs(data, d, count + 1, costs, history)


def do1(data: list[str]):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "E":
                end = (x, y)
    costs: dict[tuple[int], int] = {}
    path: set[tuple] = set()
    get_all_costs(data, end, 0, costs, path)
    count = 0
    need_to_save = 100
    for pos in path:
        if pos == end:
            continue
        for d in [
            [(pos[0], pos[1] - 2), (pos[0], pos[1] - 1)],
            [(pos[0] + 2, pos[1]), (pos[0] + 1, pos[1])],
            [(pos[0], pos[1] + 2), (pos[0], pos[1] + 1)],
            [(pos[0] - 2, pos[1]), (pos[0] - 1, pos[1])],
        ]:
            jump = d[0]
            wall = d[1]
            if not (0 <= jump[0] < len(data[0]) and 0 <= jump[1] < len(data)):
                continue
            if jump not in path:
                continue
            if data[wall[1]][wall[0]] != "#":
                continue
            old = costs[pos]
            saved = old - costs[jump] - 2
            if saved >= need_to_save:
                count += 1

    print(count)


def do2(data: list[str]):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "E":
                end = (x, y)
    costs: dict[tuple[int], int] = {}
    path: set[tuple] = set()
    get_all_costs(data, end, 0, costs, path)
    count = 0
    need_to_save = 100
    for pos in path:
        if pos == end:
            continue
        can_reach = set()
        for x in range(-20, 21):
            for y in range(-20 + abs(x), 20 - abs(x) + 1):
                can_reach.add((pos[0] + x, pos[1] + y, abs(x) + abs(y)))
        for d in can_reach:
            jump = (d[0], d[1])
            if not (0 <= jump[0] < len(data[0]) and 0 <= jump[1] < len(data)):
                continue
            if jump not in path:
                continue
            old = costs[pos]
            saved = old - costs[jump] - d[2]
            if saved >= need_to_save:
                count += 1

    print(count)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
