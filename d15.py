from pathlib import Path
from dataclasses import dataclass


def box_moves_p1(walls: set[tuple[int]], boxes: set[tuple[int]], pos: tuple[int], diff: tuple[int]) -> list[tuple[int]]:
    next_pos = pos
    to_move: list[tuple[int]] = []
    while next_pos not in walls:
        if next_pos not in boxes:
            return to_move
        to_move.append(next_pos)
        next_pos = (next_pos[0] + diff[0], next_pos[1] + diff[1])
    return []


def do1(data: list[str]):
    walls: set[tuple[int]] = set()
    boxes: set[tuple[int]] = set()
    robot = (-1, -1)
    max_x = len(data[0])
    max_y = data.index("")

    for y in range(max_y):
        for x in range(max_x):
            char = data[y][x]
            if char == "#":
                walls.add((x, y))
            elif char == "@":
                robot = (x, y)
            elif char == "O":
                boxes.add((x, y))

    moves = [item for sublist in data[max_y + 1:] for item in list(sublist)]
    for m in moves:
        if m == "^":
            diff = (0, -1)
        elif m == ">":
            diff = (1, 0)
        elif m == "v":
            diff = (0, 1)
        else:
            diff = (-1, 0)
        next_pos = (robot[0] + diff[0], robot[1] + diff[1])

        # next to a wall?
        if next_pos in walls:
            continue
        # next to free space?
        if next_pos not in boxes:
            robot = next_pos
            continue

        to_move = box_moves_p1(walls, boxes, next_pos, diff)
        if to_move:
            robot = next_pos

        for b in to_move:
            boxes.remove(b)
        for b in to_move:
            boxes.add((b[0] + diff[0], b[1] + diff[1]))
    total = 0
    for b in boxes:
        total += b[0] + (b[1] * 100)

    print(total)


def box_moves_p2(walls: set[tuple[int]], boxes: set[tuple[int]], pos: tuple[int], diff: tuple[int]) -> list[tuple[int]]:
    to_move: set[tuple[int]] = set()
    to_check: list[tuple[int]] = []
    to_check.append(pos)
    checked: set[tuple[int]] = set()
    while to_check:
        cur_pos = to_check.pop()
        checked.add(cur_pos)
        if (cur_pos[0], cur_pos[1]) in walls:
            return set()
        if (cur_pos[0], cur_pos[1], 0) not in boxes and (cur_pos[0], cur_pos[1], 1) not in boxes:
            continue
        cur_box_half = (cur_pos[0], cur_pos[1], 0) if (
            cur_pos[0], cur_pos[1], 0) in boxes else (cur_pos[0], cur_pos[1], 1)
        x_diff = 1 if cur_box_half[2] == 0 else -1
        cur_box_other_half = (cur_pos[0] + x_diff,
                              cur_pos[1], int(not cur_box_half[2]))
        checked.add((cur_box_other_half[0], cur_box_other_half[1]))
        to_move.add(cur_box_half)
        to_move.add(cur_box_other_half)
        for x in [(cur_box_half[0] + diff[0], cur_box_half[1] + diff[1]), (cur_box_other_half[0] + diff[0], cur_box_other_half[1] + diff[1])]:
            if x not in checked:
                to_check.append(x)
    return to_move


def do2(data: list[str]):
    walls: set[tuple[int]] = set()
    boxes: set[tuple[int]] = set()
    robot = (-1, -1)
    max_x = len(data[0])
    max_y = data.index("")
    total = 0

    for y in range(max_y):
        for x in range(max_x):
            char = data[y][x]
            if char == "#":
                walls.add((x * 2, y))
                walls.add(((x * 2) + 1, y))
            elif char == "@":
                robot = (x * 2, y)
            elif char == "O":
                boxes.add((x * 2, y, 0))
                boxes.add(((x * 2) + 1, y, 1))

    moves = [item for sublist in data[max_y + 1:] for item in list(sublist)]
    for m in moves:
        if m == "^":
            diff = (0, -1)
        elif m == ">":
            diff = (1, 0)
        elif m == "v":
            diff = (0, 1)
        else:
            diff = (-1, 0)
        next_pos = (robot[0] + diff[0], robot[1] + diff[1])

        # next to a wall?
        if next_pos in walls:
            continue
        # next to free space?
        if (next_pos[0], next_pos[1], 0) not in boxes and (next_pos[0], next_pos[1], 1) not in boxes:
            robot = next_pos
            continue

        to_move = box_moves_p2(walls, boxes, next_pos, diff)
        if to_move:
            robot = next_pos

        for b in to_move:
            boxes.remove(b)
        for b in to_move:
            boxes.add((b[0] + diff[0], b[1] + diff[1], b[2]))

    for b in boxes:
        if b[2] == 1:
            continue
        total += b[0] + (b[1] * 100)

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
