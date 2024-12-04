from pathlib import Path


def do1(data: list[str]):
    print("done")


def do2(data: list[str]):
    print("done")


def wrapper():
    test = True
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do1(data)


if __name__ == '__main__':
    wrapper()
