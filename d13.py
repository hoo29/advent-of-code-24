from pathlib import Path
from collections import defaultdict
from scipy.optimize import linprog


def search(a: list[int], b: list[int], prize: list[int], cost: int, x: int, y: int, steps: int, history: dict[str, int]):
    pos_str = f"{x},{y}"

    if steps > 200:
        return
    if x > prize[0] or y > prize[1]:
        return
    if history[pos_str] <= cost:
        return
    history[pos_str] = cost
    if x == prize[0] and y == prize[1]:
        print("prize")
        return
    search(a, b, prize, cost + 1, x + b[0], y + b[1], steps + 1, history)
    search(a, b, prize, cost + 3, x + a[0], y + a[1], steps + 1, history)


def do1(data: list[str]):

    games = []
    for i in range(0, len(data), 4):
        a = data[i]
        b = data[i + 1]
        prize = data[i + 2]

        a = a.split(":")[1].split(",")
        a = [int(p[2:]) for p in a]
        b = b.split(":")[1].split(",")
        b = [int(p[2:]) for p in b]

        prize = prize.split(":")[1].split(",")
        prize = [int(p[3:]) for p in prize]
        games.append([
            a, b, prize
        ])

    total = 0
    for game in games:
        history: dict[str, int] = defaultdict(lambda: float('inf'))
        search(game[0], game[1], game[2], 0, 0, 0, 0, history)
        cheapest = history.get(f"{game[2][0]},{game[2][1]}")
        if cheapest:
            total += cheapest
    print(total)


# shamelessly taken from the reddit post explaining how to do maths
def solve(a: list[int], b: list[int], prize: list[int]):

    det = a[0] * b[1] - a[1] * b[0]
    ax = (prize[0] * b[1] - prize[1] * b[0]) // det
    by = (a[0] * prize[1] - a[1] * prize[0]) // det
    if (a[0] * ax + b[0] * by, a[1] * ax + b[1] * by) == (prize[0], prize[1]):
        return ax * 3 + by
    else:
        return 0


def do2(data: list[str]):

    games = []
    for i in range(0, len(data), 4):
        a = data[i]
        b = data[i + 1]
        prize = data[i + 2]

        a = a.split(":")[1].split(",")
        a = [int(p[2:]) for p in a]
        b = b.split(":")[1].split(",")
        b = [int(p[2:]) for p in b]

        prize = prize.split(":")[1].split(",")
        prize = [int(p[3:]) for p in prize]
        prize = [x + 10000000000000 for x in prize]
        games.append([
            a, b, prize
        ])

    total = 0
    for game in games:
        total += solve(game[0], game[1], game[2])

    print(total)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
