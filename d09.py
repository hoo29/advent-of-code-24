from pathlib import Path


def do1(data: list[str]):
    line = [int(x) for x in data[0]]
    disk: list[str] = []
    ind = 0
    id = 0
    while True:
        block_count = line[ind]
        for _ in range(block_count):
            disk.append(str(id))
        id += 1
        ind += 1
        if ind >= len(line):
            break
        free_space = line[ind]
        for _ in range(free_space):
            disk.append(".")
        ind += 1
        if ind >= len(line):
            break
    dot_ind = disk.index(".")
    dig_ind = len(disk) - 1
    while dig_ind > dot_ind:
        disk[dot_ind] = disk[dig_ind]
        disk[dig_ind] = "."
        while dig_ind > dot_ind and disk[dot_ind] != ".":
            dot_ind += 1
        while dig_ind > dot_ind and disk[dig_ind] == ".":
            dig_ind -= 1
    count = 0
    # print("".join(disk))
    for ind, idk in enumerate(disk):
        if idk == ".":
            break
        count += ind * int(idk)
    print(count)


def do2(data: list[str]):
    line = [int(x) for x in data[0]]
    disk: list[str] = []
    ind = 0
    id = 0
    all_block_count: dict[int, int] = {}
    while True:
        block_count = line[ind]
        all_block_count[id] = block_count
        for _ in range(block_count):
            disk.append(str(id))
        id += 1
        ind += 1
        if ind >= len(line):
            break
        free_space = line[ind]
        for _ in range(free_space):
            disk.append(".")
        ind += 1
        if ind >= len(line):
            break
    id -= 1
    dot_ind = disk.index(".")
    while id >= 0:
        print(id)
        dig_ind = disk.index(str(id))
        block_count = all_block_count[id]
        can_move = False
        for dot_ind in range(len(disk) - block_count):
            if dot_ind > dig_ind:
                break
            if all(x == "." for x in disk[dot_ind: dot_ind + block_count]):
                can_move = True
                break
        if can_move:
            for _ in range(block_count):
                disk[dot_ind] = disk[dig_ind]
                disk[dig_ind] = "."
                dot_ind += 1
                dig_ind += 1
        id -= 1

    count = 0
    # print("".join(disk))
    for ind, idk in enumerate(disk):
        if idk == ".":
            continue
        count += ind * int(idk)
    print(count)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]
    # I've waited longer
    do2(data)


if __name__ == '__main__':
    wrapper()
