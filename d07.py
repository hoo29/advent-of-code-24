from pathlib import Path


def add_mask_p1(mask: list[str], ind=0):
    if ind == len(mask):
        return None

    if mask[ind] == "+":
        mask[ind] = "*"
    elif mask[ind] == "*":
        mask[ind] = "+"
        return add_mask_p1(mask, ind + 1)

    return mask


def do1(data: list[str]):
    sum = 0
    for line in data:
        parts = line.split(": ")
        desired_res = int(parts[0])
        values = [int(x) for x in parts[1].split(" ")]
        mask = ["+" for _ in range(len(values) - 1)]
        while mask:
            res = values[0]
            for ind, op in enumerate(mask):
                if op == "+":
                    res += values[ind + 1]
                elif op == "*":
                    res *= values[ind + 1]
            if res == desired_res:
                sum += res
                break
            mask = add_mask_p1(mask)
    print(sum)


def add_mask_p2(mask: list[str], ind=0):
    if ind == len(mask):
        return None

    if mask[ind] == "+":
        mask[ind] = "*"
    elif mask[ind] == "*":
        mask[ind] = "||"
    else:
        mask[ind] = "+"
        return add_mask_p2(mask, ind + 1)

    return mask


def do2(data: list[str]):
    sum = 0
    for prog, line in enumerate(data):
        print(f"line {prog} of {len(data)}")
        parts = line.split(": ")
        desired_res = int(parts[0])
        values = [int(x) for x in parts[1].split(" ")]
        mask = ["+" for _ in range(len(values) - 1)]
        while mask:
            res = values[0]
            for ind, op in enumerate(mask):
                if op == "+":
                    res += values[ind + 1]
                elif op == "*":
                    res *= values[ind + 1]
                elif op == "||":
                    res *= 10 ** len(str(values[ind + 1]))
                    res += values[ind + 1]
            if res == desired_res:
                sum += res
                break
            mask = add_mask_p2(mask)
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
