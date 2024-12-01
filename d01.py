from pathlib import Path
from collections import Counter


def do(data: list[str]):
    l1 = []
    l2 = []
    for x in data:
        parts = x.split(" ")
        l1.append(int(parts[0]))
        l2.append(int(parts[-1]))
    l1.sort()
    l2.sort()

    diff = sum(abs(x - y) for x, y in zip(l1, l2))
    print(diff)

    appears = Counter(l2)
    sim = sum(x * appears[x] for x in l1)
    print(sim)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do(data)


if __name__ == '__main__':
    wrapper()
