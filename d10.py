from pathlib import Path


def do1(data: list[str]):
    grid: list[list[int]] = []
    for l in data:
        grid.append([int(x) if x != "." else -1 for x in l])

    start_positions: list[tuple[int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                start_positions.append((x, y))
    count = 0
    while start_positions:
        to_explore = [start_positions.pop()]
        reached = []
        while to_explore:
            x, y = to_explore.pop()
            cur_num = grid[y][x]
            for next_pos in [[x, y - 1], [x + 1, y], [x, y + 1], [x - 1, y]]:
                if next_pos[0] < 0 or next_pos[1] < 0:
                    continue
                if next_pos[0] >= len(grid[0]) or next_pos[1] >= len(grid):
                    continue
                next_num = grid[next_pos[1]][next_pos[0]]
                if cur_num == 8 and next_num == 9:
                    if next_pos not in reached:
                        reached.append(next_pos)
                        count += 1
                elif next_num == cur_num + 1:
                    to_explore.append(next_pos)

    print(count)


def do2(data: list[str]):
    grid: list[list[int]] = []
    for l in data:
        grid.append([int(x) if x != "." else -1 for x in l])

    start_positions: list[tuple[int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                start_positions.append((x, y))
    count = 0
    while start_positions:
        to_explore = [start_positions.pop()]
        while to_explore:
            x, y = to_explore.pop()
            cur_num = grid[y][x]
            for next_pos in [[x, y - 1], [x + 1, y], [x, y + 1], [x - 1, y]]:
                if next_pos[0] < 0 or next_pos[1] < 0:
                    continue
                if next_pos[0] >= len(grid[0]) or next_pos[1] >= len(grid):
                    continue
                next_num = grid[next_pos[1]][next_pos[0]]
                if cur_num == 8 and next_num == 9:
                    count += 1
                elif next_num == cur_num + 1:
                    to_explore.append(next_pos)

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
