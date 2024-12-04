from pathlib import Path


def do1(data: list[str]):
    word = "XMAS"
    count = 0
    for y, _ in enumerate(data):
        for x, _ in enumerate(data[y]):
            if data[y][x] != "X":
                continue
            direction = 0
            word_ind = 1
            sub_y = y
            sub_x = x
            while direction < 8:
                # n
                if direction == 0:
                    sub_y = y - word_ind
                    sub_x = x
                # ne
                elif direction == 1:
                    sub_y = y - word_ind
                    sub_x = x + word_ind
                # e
                elif direction == 2:
                    sub_y = y
                    sub_x = x + word_ind
                # se
                elif direction == 3:
                    sub_y = y + word_ind
                    sub_x = x + word_ind
                # s
                elif direction == 4:
                    sub_y = y + word_ind
                    sub_x = x
                # sw
                elif direction == 5:
                    sub_y = y + word_ind
                    sub_x = x - word_ind
                # w
                elif direction == 6:
                    sub_y = y
                    sub_x = x - word_ind
                # nw
                elif direction == 7:
                    sub_y = y - word_ind
                    sub_x = x - word_ind

                if (
                        sub_y < 0 or
                        sub_y >= len(data) or
                        sub_x < 0 or
                        sub_x >= len(data[0]) or
                        data[sub_y][sub_x] != word[word_ind]
                ):
                    direction += 1
                    word_ind = 1
                else:
                    word_ind += 1

                if word_ind == len(word):
                    count += 1
                    direction += 1
                    word_ind = 1

    print(count)


def do2(data: list[str]):
    count = 0
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):

            if (
                data[y - 1][x - 1] == "M" and
                data[y - 1][x + 1] == "S" and
                data[y][x] == "A" and
                data[y + 1][x - 1] == "M" and
                data[y + 1][x + 1] == "S"
            ):
                count += 1

            if (
                data[y - 1][x - 1] == "S" and
                data[y - 1][x + 1] == "S" and
                data[y][x] == "A" and
                data[y + 1][x - 1] == "M" and
                data[y + 1][x + 1] == "M"
            ):
                count += 1

            if (
                data[y - 1][x - 1] == "M" and
                data[y - 1][x + 1] == "M" and
                data[y][x] == "A" and
                data[y + 1][x - 1] == "S" and
                data[y + 1][x + 1] == "S"
            ):
                count += 1

            if (
                data[y - 1][x - 1] == "S" and
                data[y - 1][x + 1] == "M" and
                data[y][x] == "A" and
                data[y + 1][x - 1] == "S" and
                data[y + 1][x + 1] == "M"
            ):
                count += 1

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
