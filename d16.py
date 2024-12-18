from pathlib import Path
from collections import defaultdict
import sys
import heapq
from collections import deque

sys.setrecursionlimit(20000)


def solve_p1(walls: tuple[int], end: tuple[int], pos: tuple[int], history: dict[tuple[int], int], dir: int, cost: int):
    if pos in walls:
        return float('inf')
    if history[(pos[0], pos[1], dir)] <= cost:
        return float('inf')
    if pos == end:
        return cost
    history[(pos[0], pos[1], dir)] = cost
    dirs = [0, 1, 2, 3]
    dirs.remove((dir + 2) % 4)
    costs = []
    for d in dirs:
        if d == 0:
            next_pos = (pos[0], pos[1] - 1)
        elif d == 1:
            next_pos = (pos[0] + 1, pos[1])
        elif d == 2:
            next_pos = (pos[0], pos[1] + 1)
        else:
            next_pos = (pos[0] - 1, pos[1])
        c = solve_p1(walls, end, next_pos, history,
                     d, cost + 1 + (1000 if d != dir else 0))
        costs.append(c)
    return min(costs)


def do1(data: list[str]):
    walls: set[tuple[int]] = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "S":
                start = (x, y)
            elif data[y][x] == "E":
                end = (x, y)
            elif data[y][x] == "#":
                walls.add((x, y))
    ans = solve_p1(walls, end, start, defaultdict(lambda: float('inf')), 1, 0)
    print(ans)
    return ans


def solve_p2(walls: tuple[int], end: tuple[int], max_cost: int, start: tuple[int], all_history: set[tuple[int]]):
    queue = [(0, 1, start, set())]
    prog = set()
    history_cost = defaultdict(lambda: float('inf'))
    while queue:
        cost, dir, pos, history = heapq.heappop(queue)
        for i in range(1, 134):
            marker = i * 1000
            if cost > marker and marker not in prog:
                print(f"cost {cost}")
                prog.add(marker)
        if pos in walls:
            continue
        if pos in history:
            continue
        if cost > max_cost:
            return
        if cost > history_cost[(pos, dir)]:
            continue
        history_cost[(pos, dir)] = cost
        history.add(pos)
        if pos == end:
            all_history.update(history)
            continue
        dirs = [0, 1, 2, 3]
        dirs.remove((dir + 2) % 4)
        for d in dirs:
            if d == 0:
                next_pos = (pos[0], pos[1] - 1)
            elif d == 1:
                next_pos = (pos[0] + 1, pos[1])
            elif d == 2:
                next_pos = (pos[0], pos[1] + 1)
            else:
                next_pos = (pos[0] - 1, pos[1])
            heapq.heappush(queue, (cost + 1 + (1000 if d != dir else 0),
                                   d, next_pos, history.copy()))


def do2(data: list[str], test: bool):
    if test:
        max_cost = do1(data)
    else:
        max_cost = 133_584
    walls: set[tuple[int]] = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "S":
                start = (x, y)
            elif data[y][x] == "E":
                end = (x, y)
            elif data[y][x] == "#":
                walls.add((x, y))
    all_history = set()
    solve_p2(walls, end, max_cost, start, all_history)
    print(len(all_history))


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data, test)


if __name__ == '__main__':
    wrapper()
