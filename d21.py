from pathlib import Path
from itertools import permutations, product
from functools import cache
numeric = {
    "A": [2, 3],
    "0": [1, 3],
    "1": [0, 2],
    "2": [1, 2],
    "3": [2, 2],
    "4": [0, 1],
    "5": [1, 1],
    "6": [2, 1],
    "7": [0, 0],
    "8": [1, 0],
    "9": [2, 0],
}

dirs = {
    "A": [2, 0],
    "^": [1, 0],
    "<": [0, 1],
    "v": [1, 1],
    ">": [2, 1],
}


def door_moves(pos: list[int], code: str):
    door_movement: list[list[str]] = []
    for dest in list(code):
        moves: list[str] = []

        if pos in [[1, 3], [2, 3]] and numeric[dest][0] == 0:
            while pos[1] > numeric[dest][1]:
                moves.append("^")
                pos[1] -= 1
                assert not (pos[0] == 0 and pos[1] == 3)

        if pos[0] == 0 and (dest == "A" or dest == "0"):
            while pos[0] < numeric[dest][0]:
                moves.append(">")
                pos[0] += 1
                assert not (pos[0] == 0 and pos[1] == 3)

        while pos[0] > numeric[dest][0]:
            moves.append("<")
            pos[0] -= 1
            assert not (pos[0] == 0 and pos[1] == 3)

        while pos[1] < numeric[dest][1]:
            moves.append("v")
            pos[1] += 1
            assert not (pos[0] == 0 and pos[1] == 3)

        while pos[0] < numeric[dest][0]:
            moves.append(">")
            pos[0] += 1
            assert not (pos[0] == 0 and pos[1] == 3)

        if pos[0] == 0 and (dest == "A" or dest == "0"):
            moves.append(">")
            pos[0] += 1
            assert not (pos[0] == 0 and pos[1] == 3)

        while pos[1] > numeric[dest][1]:
            moves.append("^")
            pos[1] -= 1
            assert not (pos[0] == 0 and pos[1] == 3)

        door_movement.append(moves)
    return door_movement


@cache
def dir_moves3(pos: tuple[int], moves: tuple[str]):
    dir_movement: list[tuple[tuple[str, ...]]] = []
    new_pos = (pos[0], pos[1])
    for seq in (*moves, "A"):
        seq_moves: list[tuple[tuple[str, ...], ...]] = []
        for dest in seq:
            dest_pos = dirs[dest]
            potential_moves: list[str] = []
            potential_moves.extend(["<"] * (new_pos[0] - dest_pos[0]))
            potential_moves.extend([">"] * (dest_pos[0] - new_pos[0]))

            potential_moves.extend(["v"] * (dest_pos[1] - new_pos[1]))
            potential_moves.extend(["^"] * (new_pos[1] - dest_pos[1]))
            all_potential_moves = list(set(permutations(potential_moves)))
            for pm in all_potential_moves:
                temp_pos = (new_pos[0], new_pos[1])
                valid = True
                for pm_move in pm:
                    if pm_move == "<":
                        temp_pos = (temp_pos[0] - 1, temp_pos[1])
                    elif pm_move == ">":
                        temp_pos = (temp_pos[0] + 1, temp_pos[1])
                    elif pm_move == "^":
                        temp_pos = (temp_pos[0], temp_pos[1] - 1)
                    elif pm_move == "v":
                        temp_pos = (temp_pos[0], temp_pos[1] + 1)
                    else:
                        raise Exception("what")
                    if temp_pos[0] < 0 or temp_pos[1] < 0:
                        raise Exception("what")
                    if temp_pos[0] == 0 and temp_pos[1] == 0:
                        valid = False
                        break
                if valid:
                    seq_moves.append(pm)
            new_pos = dest_pos
        dir_movement.append(tuple(seq_moves))
        ret = tuple(dir_movement)
    return (ret, new_pos)


@cache
def search(max_depth: int, depth: int, moves: tuple[tuple[str, ...]]) -> int:
    count = 0
    if depth == max_depth:
        return sum([len(x) + 1 for x in moves])
    for m in moves:
        next_moves, _ = dir_moves3((2, 0), m)
        count += min([search(max_depth, depth + 1, x)
                     for x in product(*next_moves)])
    return count


def do2(data: list[str]):
    ans = 0
    robot_count = 25
    c = data
    new_ans = 0
    for code in c:
        door = [2, 3]
        door_movement = door_moves(door, code)
        door_movement_tuple = tuple([tuple(x) for x in door_movement])
        new_count = search(robot_count, 0, door_movement_tuple)
        new_ans += int(code[:-1]) * new_count

    print(new_ans)


def do1(data: list[str]):
    ans = 0
    for code in data:
        rob0 = [2, 0]
        rob1 = [2, 0]
        door = [2, 3]
        door_movement = door_moves(door, code)
        # print()
        rob0_movement = dir_moves(rob0, door_movement)
        # print()
        rob1_movement = dir_moves(rob1, rob0_movement)
        move_count = sum([len(x) + 1 for x in rob1_movement])
        print()
        output = ""
        for mov in rob1_movement:
            for m in mov:
                output += m
            output += "A"
        print(output)
        print(move_count)
        ans += int(code[:-1]) * move_count

    print()
    print(ans)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
