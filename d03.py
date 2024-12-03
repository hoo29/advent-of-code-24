from pathlib import Path
import re


def do1(data: list[str]):
    prog = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    line = "".join(data)
    sum = 0
    for r in re.findall(prog, line):
        op1 = int(r.split(",")[0][4:])
        op2 = int(r.split(",")[1][:-1])
        sum += op1 * op2
    print(sum)


def do2(data: list[str]):
    line = "".join(data)
    idx = 0
    sum = 0
    enabled = True
    prog = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    while idx < len(line):
        match = prog.match(line[idx:idx+12])
        if line[idx:idx+4] == "do()":
            enabled = True
            idx += 4
        elif line[idx:idx+7] == "don't()":
            enabled = False
            idx += 7
        elif match:
            if enabled:
                op1 = int(match.group(0).split(",")[0][4:])
                op2 = int(match.group(0).split(",")[1][:-1])
                sum += op1 * op2
            idx += len(match.group(0))
        else:
            idx += 1
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
