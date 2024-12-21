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


def dir_moves(pos: list[int], moves: list[list[str]], back_to_a=True):
    dir_movement: list[list[str]] = []
    moves_with_a = []
    for m in moves:
        moves_with_a.append(m)
        if back_to_a:
            moves_with_a.append(["A"])

    for seq in moves_with_a:
        for dest in seq:
            moves: list[str] = []
            if dest == "<" and pos[1] == 0:
                moves.append("v")
                pos[1] += 1
                assert not (pos[0] == 0 and pos[1] == 0)

            while pos[0] > dirs[dest][0]:
                moves.append("<")
                pos[0] -= 1
                assert not (pos[0] == 0 and pos[1] == 0)

            while pos[1] < dirs[dest][1]:
                moves.append("v")
                pos[1] += 1

            if pos[0] == 0 and (dest == "A" or dest == "^"):
                moves.append(">")
                pos[0] += 1
                assert not (pos[0] == 0 and pos[1] == 0)

            while pos[0] < dirs[dest][0]:
                moves.append(">")
                pos[0] += 1
                assert not (pos[0] == 0 and pos[1] == 0)

            while pos[1] > dirs[dest][1]:
                moves.append("^")
                pos[1] -= 1
                assert not (pos[0] == 0 and pos[1] == 0)

            dir_movement.append(moves)
    return dir_movement


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
    print("done")


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do1(data)


if __name__ == '__main__':
    wrapper()
