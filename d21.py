from pathlib import Path
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

# go left, down, right, up


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

        # print(moves)
        door_movement.append(moves)
    return door_movement


def dir_moves(pos: tuple[int], moves: list[list[str]], cache: dict):
    dir_movement: list[list[str]] = []
    moves_with_a = []
    for m in moves:
        moves_with_a.append(m)
        moves_with_a.append(["A"])
    new_pos = (pos[0], pos[1])
    for seq in moves_with_a:

        key = f"{new_pos[0], new_pos[1]},{"".join(seq)}"
        if key in cache:
            item = cache[key]
            dir_movement += item[0]
            new_pos = item[1]
        else:
            seq_moves = []
            for dest in seq:
                moves: list[str] = []
                if dest == "<" and new_pos[1] == 0:
                    moves.append("v")
                    new_pos = (new_pos[0], new_pos[1] + 1)
                    assert not (new_pos[0] == 0 and new_pos[1] == 0)

                while new_pos[0] > dirs[dest][0]:
                    moves.append("<")
                    new_pos = (new_pos[0] - 1, new_pos[1])
                    assert not (new_pos[0] == 0 and new_pos[1] == 0)

                while new_pos[1] < dirs[dest][1]:
                    moves.append("v")
                    new_pos = (new_pos[0], new_pos[1] + 1)

                if new_pos[0] == 0 and (dest == "A" or dest == "^"):
                    moves.append(">")
                    new_pos = (new_pos[0] + 1, new_pos[1])
                    assert not (new_pos[0] == 0 and new_pos[1] == 0)

                while new_pos[0] < dirs[dest][0]:
                    moves.append(">")
                    new_pos = (new_pos[0] + 1, new_pos[1])
                    assert not (new_pos[0] == 0 and new_pos[1] == 0)

                while new_pos[1] > dirs[dest][1]:
                    moves.append("^")
                    new_pos = (new_pos[0], new_pos[1] - 1)
                    assert not (new_pos[0] == 0 and new_pos[1] == 0)

                seq_moves.append(moves)

            dir_movement += seq_moves
            cache[key] = [seq_moves, new_pos]
    return [dir_movement, new_pos]


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


def do2(data: list[str]):
    ans = 0
    robot_count = 2

    for code in data:
        door = [2, 3]
        door_movement = door_moves(door, code)
        robots = [(2, 0) for _ in range(robot_count)]
        last = door_movement
        cache = {}
        for ind in range(robot_count):
            print(ind)
            last, pos = dir_moves(robots[ind], last, cache)
            robots[ind] = pos

        move_count = sum([len(x) + 1 for x in last])
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
