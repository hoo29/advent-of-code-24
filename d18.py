from pathlib import Path
from collections import defaultdict

import sys


sys.setrecursionlimit(20000)


def solve_p1(fallen: set[str], end: tuple[int], pos: tuple[int], history: dict[str, int], steps: int):

    if pos[0] < 0 or pos[0] > end[0] or pos[1] < 0 or pos[1] > end[1]:
        return float('inf')
    pos_str = f"{pos[0]},{pos[1]}"
    if history[pos_str] <= steps:
        return float('inf')
    history[pos_str] = steps
    if pos == end:
        return steps
    if pos_str in fallen:
        return float('inf')

    all_steps = []
    for next_pos in [
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1])
    ]:
        c = solve_p1(fallen, end, next_pos, history, steps + 1)
        all_steps.append(c)
    return min(all_steps)


def do1(data: list[str], test: bool):
    max_pos = 70 if not test else 6
    all_bytes = data
    history: dict[str, int] = defaultdict(lambda: float('inf'))
    fallen = set(all_bytes[:1024 if not test else 12])
    ans = solve_p1(fallen, (max_pos, max_pos), (0, 0), history, 0)
    print(ans)


def solve_p2(fallen: set[str], end: tuple[int], pos: tuple[int], history: dict[str, int], steps: int):

    if pos[0] < 0 or pos[0] > end[0] or pos[1] < 0 or pos[1] > end[1]:
        return float('inf')
    pos_str = f"{pos[0]},{pos[1]}"
    if history[pos_str] <= steps:
        return float('inf')
    history[pos_str] = steps
    if pos == end:
        return steps
    if pos_str in fallen:
        return float('inf')

    all_steps = []
    for next_pos in [
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1])
    ]:
        c = solve_p2(fallen, end, next_pos, history, steps + 1)
        all_steps.append(c)
    return min(all_steps)


def do2(data: list[str], test: bool):
    max_pos = 70 if not test else 6
    all_bytes = data
    byte = 3000
    while True and byte <= len(all_bytes):
        print(byte)
        history: dict[str, int] = defaultdict(lambda: float('inf'))
        fallen = set(all_bytes[:byte if not test else 21])
        ans = solve_p2(fallen, (max_pos, max_pos), (0, 0), history, 0)
        if ans == float('inf'):
            print("done")
            print(all_bytes[byte - 1])
            break
        else:
            byte += 1
    print(byte)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data, test)


if __name__ == '__main__':
    wrapper()
