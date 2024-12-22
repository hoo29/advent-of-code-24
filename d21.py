from pathlib import Path
from collections import deque, defaultdict
from copy import deepcopy
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
    moves_with_a: list[list[str]] = []

    key = f"{pos[0]},{pos[1]},{"".join([str(x) for x in moves])}"
    # key = (pos, tuple(map(tuple, moves)))
    new_pos = (pos[0], pos[1])
    # if key in cache:
    #     print("cache")
    #     return cache[key]
    for m in moves:
        moves_with_a.append(m)
        moves_with_a.append(["A"])

    for seq in moves_with_a:
        seq_moves = []
        for dest in seq:
            sub_moves: list[str] = []
            if dest == "<" and new_pos[1] == 0:
                sub_moves.append("v")
                new_pos = (new_pos[0], new_pos[1] + 1)
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[0] > dirs[dest][0]:
                sub_moves.append("<")
                new_pos = (new_pos[0] - 1, new_pos[1])
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[1] < dirs[dest][1]:
                sub_moves.append("v")
                new_pos = (new_pos[0], new_pos[1] + 1)
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            if new_pos[0] == 0 and (dest == "A" or dest == "^"):
                sub_moves.append(">")
                new_pos = (new_pos[0] + 1, new_pos[1])
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[0] < dirs[dest][0]:
                sub_moves.append(">")
                new_pos = (new_pos[0] + 1, new_pos[1])
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[1] > dirs[dest][1]:
                sub_moves.append("^")
                new_pos = (new_pos[0], new_pos[1] - 1)
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            seq_moves.append(sub_moves)

        dir_movement += seq_moves
    cache[key] = (dir_movement, new_pos)
    return (dir_movement, new_pos)


dd = [2, 3]
dr0 = [2, 0]
dr1 = [2, 0]


def debug_the_things(movements: list[str]):
    _dmoves = {
        "^": [0, -1],
        "<": [-1, 0],
        "v": [0, 1],
        ">": [1, 0],
    }
    for m in movements:
        dr0[0] += _dmoves[m][0]
        dr0[1] += _dmoves[m][1]
    direction = [k for k, v in dirs.items() if v == dr0][0]
    print(f"robot 0 at {dr0} {direction}")
    if direction != "A":
        dr1[0] += _dmoves[direction][0]
        dr1[1] += _dmoves[direction][1]
    if direction == "A":
        print(f"robot 0 presses A")

        direction2 = [k for k, v in dirs.items() if v == dr1][0]
        print(f"robot 1 at {dr1} {direction2}")
        if direction2 != "A":
            dd[0] += _dmoves[direction2][0]
            dd[1] += _dmoves[direction2][1]
        num = [k for k, v in numeric.items() if v == dd][0]

        if direction2 == "A":
            print(f"door pressed {dd} {num}")
        else:
            print(f"door at {dd} {num}")
    print("")


def dir_moves2(pos: tuple[int], moves: list[list[str]]):
    dir_movement: list[list[str]] = []
    moves_with_a: list[list[str]] = []

    key = f"{pos[0]},{pos[1]},{"".join([str(x) for x in moves])}"
    # key = (pos, tuple(map(tuple, moves)))
    new_pos = (pos[0], pos[1])
    # if key in cache:
    #     print("cache")
    #     return cache[key]
    moves_with_a = moves.copy()
    moves_with_a.append(["A"])

    for seq in moves_with_a:
        seq_moves = []
        for dest in seq:
            sub_moves: list[str] = []
            if dest == "<" and new_pos[1] == 0:
                sub_moves.append("v")
                new_pos = (new_pos[0], new_pos[1] + 1)
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[0] > dirs[dest][0]:
                sub_moves.append("<")
                new_pos = (new_pos[0] - 1, new_pos[1])
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[1] < dirs[dest][1]:
                sub_moves.append("v")
                new_pos = (new_pos[0], new_pos[1] + 1)
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            if new_pos[0] == 0 and (dest == "A" or dest == "^"):
                sub_moves.append(">")
                new_pos = (new_pos[0] + 1, new_pos[1])
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[0] < dirs[dest][0]:
                sub_moves.append(">")
                new_pos = (new_pos[0] + 1, new_pos[1])
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            while new_pos[1] > dirs[dest][1]:
                sub_moves.append("^")
                new_pos = (new_pos[0], new_pos[1] - 1)
                assert not (new_pos[0] == 0 and new_pos[1] == 0)

            seq_moves.append(sub_moves)

        dir_movement += seq_moves
    # cache[key] = (dir_movement, new_pos)
    return (dir_movement, new_pos)


def do2(data: list[str]):
    ans = 0
    robot_count = 7
    better_cache = {}
    count = 0
    another_cache_for_some_reason = defaultdict(int)
    cache_count = 0
    c = [data[1]]
    for code in c:
        door = [2, 3]
        door_movement = door_moves(door, code)
        q = deque()
        for x in door_movement:
            q.append((0, x, []))

        robots = [(2, 0) for _ in range(robot_count)]

        while q:
            item = q.popleft()
            ind = item[0]
            movements = item[1]
            if ind == robot_count:
                count += len(movements) + 1
                for other_h in item[2]:
                    p = other_h[0]
                    seq = other_h[1]
                    pp = other_h[2]
                    key = f"{p},{pp[0]},{pp[1]},{
                        "".join([str(x) for x in seq])}"
                    another_cache_for_some_reason[key] += len(movements) + 1
                for sub_ind in range(robot_count - 1, -1, -1):
                    if q and q[0][0] < sub_ind:
                        h = item[2][sub_ind]
                        p = h[0]
                        seq = h[1]
                        pp = h[2]
                        key = f"{p},{pp[0]},{pp[1]},{
                            "".join([str(x) for x in seq])}"
                        better_cache[key] = another_cache_for_some_reason[key]
                        del another_cache_for_some_reason[key]
                continue
            original_pos = robots[ind]
            key = f"{ind},{original_pos[0]},{original_pos[1]},{
                "".join([str(x) for x in movements])}"
            if key in better_cache:
                # print(f"cache hit {key}")
                cache_count = better_cache[key] + count
                # continue

            last, pos = dir_moves2(original_pos, movements)
            for l in reversed(last):
                history = deepcopy(item[2])
                history.append([ind, movements, original_pos])
                q.appendleft((ind + 1, l, history))

            robots[ind] = pos

    for code in c:
        door = [2, 3]
        door_movement = door_moves(door, code)
        robots = [(2, 0) for _ in range(robot_count)]
        last = door_movement
        cache = {}
        for ind in range(robot_count):
            # print(ind)
            last, pos = dir_moves(robots[ind], last, cache)
            robots[ind] = pos

        move_count = sum([len(x) + 1 for x in last])
        ans += int(code[:-1]) * move_count

    print(f"new - {count}")
    print(f"c - {cache_count}")
    print(f"old - {move_count}")
    print()
    # print(ans)


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
    test = True
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
