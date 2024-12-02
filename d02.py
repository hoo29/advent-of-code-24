from pathlib import Path


def do1(data: list[str]):
    count = 0
    for line in data:
        nums = [int(x) for x in line.split(" ")]
        inc = nums[1] > nums[0]
        dec = nums[1] < nums[0]
        if not inc and not dec:
            continue
        valid = True
        for ind in range(1, len(nums)):
            a = nums[ind]
            b = nums[ind - 1]
            if inc and 1 <= a - b <= 3:
                continue
            if dec and 1 <= b - a <= 3:
                continue
            valid = False
            break

        if valid:
            count += 1

    print(count)


def check(nums: list[int]):
    inc = nums[1] > nums[0]
    dec = nums[1] < nums[0]
    if not inc and not dec:
        return False
    for ind in range(1, len(nums)):
        a = nums[ind]
        b = nums[ind - 1]
        if inc and 1 <= a - b <= 3:
            continue
        if dec and 1 <= b - a <= 3:
            continue
        return False
    return True


def do2(data: list[str]):
    count = 0

    for line in data:
        nums = [int(x) for x in line.split(" ")]
        valid = check(nums)
        if valid:
            count += 1
        else:
            for ind in range(len(nums)):
                sub_nums = nums[: ind] + nums[ind + 1:]
                if check(sub_nums):
                    count += 1
                    break

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
