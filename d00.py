from pathlib import Path


def do(data: list[str]):
    print("done")


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do(data)


if __name__ == '__main__':
    wrapper()
