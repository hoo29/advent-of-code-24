from pathlib import Path


def do1(data: list[str]):
    patterns = set(data[0].split(", "))
    designs = data[2:]
    count = 0
    longest_pattern = max([len(x) for x in list(patterns)])
    for d in designs:
        queue: list[list[int, list[str]]] = []
        queue.append([
            0,
            ""
        ])
        while queue:
            ind, history = queue.pop()
            if ind == len(d):
                print(f"{d} - {history}")
                count += 1
                break
            for i in range(min(len(d) - ind, longest_pattern)):
                sub = d[ind:ind + i + 1]
                if sub in patterns:
                    queue.append([
                        ind + i + 1,
                        history + " " + sub
                    ])

    print(count)


def do2(data: list[str]):
    patterns = set(data[0].split(", "))
    designs = data[2:]
    history: dict[str, int] = {}

    def search(d: str):
        if d in history:
            return history[d]
        count = 0 if d else 1
        for pattern in patterns:
            if d.startswith(pattern):
                count += search(d[len(pattern):])
        history[d] = count
        return count
    total = sum([search(d) for d in designs])
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
