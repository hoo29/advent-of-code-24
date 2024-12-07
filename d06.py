from pathlib import Path
import copy


def do1(data: list[str]):
    x = -1
    y = -1
    for yind, _y in enumerate(data):
        for xind, _x in enumerate(_y):
            if _x == "^":
                x = xind
                y = yind

    direction = 0
    visited = set()
    while True:
        visited.add(f"{x},{y}")
        newx = x
        newy = y
        if direction == 0:
            newy -= 1
        elif direction == 1:
            newx += 1
        elif direction == 2:
            newy += 1
        elif direction == 3:
            newx -= 1
        if newx < 0 or newy < 0 or newx >= len(data[0]) or newy >= len(data):
            break
        if data[newy][newx] != "#":
            x = newx
            y = newy
        else:
            direction = (direction + 1) % 4
    print(len(visited))


# no judge
def do2(data: list[str]):
    x = -1
    y = -1
    for yind, _y in enumerate(data):
        for xind, _x in enumerate(_y):
            if _x == "^":
                x = xind
                y = yind
                break
        if x != -1 and y != -1:
            break

    direction = 0
    visited = []
    details = []
    while True:
        if f"{x},{y}" not in visited:
            visited.append(f"{x},{y}")
        details.append(f"{x},{y},{direction}")
        newx = x
        newy = y
        if direction == 0:
            newy -= 1
        elif direction == 1:
            newx += 1
        elif direction == 2:
            newy += 1
        elif direction == 3:
            newx -= 1
        if newx < 0 or newy < 0 or newx >= len(data[0]) or newy >= len(data):
            break
        if data[newy][newx] != "#":
            x = newx
            y = newy
        else:
            direction = (direction + 1) % 4

    to_check = []
    for ind, v in enumerate(visited[1:]):
        new_data = copy.deepcopy(data)
        parts = list(map(int, v.split(",")))
        new_line = list(new_data[parts[1]])
        new_line[parts[0]] = "#"

        new_data[parts[1]] = "".join(new_line)
        old_pos = details[ind].split(",")

        to_check.append([
            new_data,
            int(old_pos[0]),  # x
            int(old_pos[1]),  # y
            int(old_pos[2]),  # d
            copy.deepcopy(details[:ind])

        ])
    total = 0
    while to_check:
        print(len(to_check))
        cur = to_check.pop()
        cur_data = cur[0]
        x = cur[1]
        y = cur[2]
        direction = cur[3]
        cur_details = set(cur[4])
        while True:
            new_details = f"{x},{y},{direction}"
            if new_details in cur_details:
                total += 1
                break
            else:
                cur_details.add(new_details)
            newx = x
            newy = y
            if direction == 0:
                newy -= 1
            elif direction == 1:
                newx += 1
            elif direction == 2:
                newy += 1
            elif direction == 3:
                newx -= 1
            if newx < 0 or newy < 0 or newx >= len(cur_data[0]) or newy >= len(cur_data):
                break
            if cur_data[newy][newx] != "#":
                x = newx
                y = newy
            else:
                direction = (direction + 1) % 4

    print("")
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
