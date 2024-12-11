from pathlib import Path
from collections import defaultdict


def do1(data: list[str]):

    stones = [int(x) for x in data[0].split(" ")]
    blinks = 25
    for ind in range(blinks):
        print(f"blink {ind}")
        new_stones: list[int] = []
        for stone in stones:
            stone_str = str(stone)
            if stone == 0:
                new_stones.append(1)
            elif len(stone_str) % 2 == 0:
                new_stones.append(int(stone_str[:len(stone_str) // 2]))
                new_stones.append(int(stone_str[len(stone_str) // 2:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    print(len(stones))


def do2(data: list[str]):
    stones = [int(x) for x in data[0].split(" ")]
    stones_cache = defaultdict(int)
    for stone in stones:
        stones_cache[stone] = 1

    blinks = 75

    for ind in range(blinks):
        print(f"blink {ind}")
        k = stones_cache.keys()
        new_stones_cache = stones_cache.copy()
        for stone in k:
            new_stones_cache[stone] -= stones_cache[stone]
            if new_stones_cache[stone] == 0:
                del new_stones_cache[stone]
            stone_str = str(stone)
            if stone == 0:
                new_stones_cache[1] += stones_cache[stone]
            elif len(stone_str) % 2 == 0:
                stone_1 = int(stone_str[:len(stone_str) // 2])
                stone_2 = int(stone_str[len(stone_str) // 2:])
                new_stones_cache[stone_1] += stones_cache[stone]
                new_stones_cache[stone_2] += stones_cache[stone]
            else:
                new_stones_cache[stone * 2024] += stones_cache[stone]

        stones_cache = new_stones_cache.copy()

    print(sum(stones_cache.values()))


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data)


if __name__ == '__main__':
    wrapper()
