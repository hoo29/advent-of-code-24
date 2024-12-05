from functools import cmp_to_key
from pathlib import Path


def do1(data: list[str], p2=False):

    ind = data.index("")
    rules = data[:ind]
    rules = [list(map(int, r.split("|"))) for r in rules]
    pages = data[ind + 1:]
    pages = [list(map(int, p.split(","))) for p in pages]

    def compare(a: int, b: int):
        for r in rules:
            if r[0] == a and r[1] == b:
                return -1
            if r[0] == b and r[1] == a:
                return 1
        return 0
    ps = [sorted(page, key=cmp_to_key(compare)) for page in pages]
    sum = 0
    for ind, page in enumerate(ps):
        if page == pages[ind] and not p2:
            sum += page[len(page) // 2]
        if page != pages[ind] and p2:
            sum += page[len(page) // 2]
    print(sum)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do1(data, True)


if __name__ == '__main__':
    wrapper()
