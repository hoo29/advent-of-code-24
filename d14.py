from pathlib import Path
from dataclasses import dataclass
import math


@dataclass
class Robot():
    x: int
    y: int
    vel_x: int
    vel_y: int


def do1(data: list[str], test: bool):
    max_x = 11 if test else 101
    max_y = 7 if test else 103
    seconds = 100

    robots: list[Robot] = []
    for line in data:
        parts = line.split(" ")
        pos = list(map(int, parts[0][2:].split(",")))
        vel = list(map(int, parts[1][2:].split(",")))
        robots.append(Robot(pos[0], pos[1], vel[0], vel[1]))

    for robot in robots:
        robot.x = (robot.x + (robot.vel_x * seconds)) % max_x
        robot.y = (robot.y + (robot.vel_y * seconds)) % max_y

    quadrants = [
        [[0, max_x // 2], [0, max_y // 2]],
        [[max_x - (max_x // 2), max_x], [0, max_y // 2]],
        [[0, max_x // 2], [max_y - (max_y // 2), max_y]],
        [[max_x - (max_x // 2), max_x], [max_y - (max_y // 2), max_y]]
    ]
    quadrant_count = [0, 0, 0, 0]
    for robot in robots:
        for ind, quad in enumerate(quadrants):
            if quad[0][0] <= robot.x < quad[0][1] and quad[1][0] <= robot.y < quad[1][1]:
                quadrant_count[ind] += 1
                continue
    print(math.prod(quadrant_count))


def do2(data: list[str], test):

    max_x = 11 if test else 101
    max_y = 7 if test else 103

    robots: list[Robot] = []
    for line in data:
        parts = line.split(" ")
        pos = list(map(int, parts[0][2:].split(",")))
        vel = list(map(int, parts[1][2:].split(",")))
        robots.append(Robot(pos[0], pos[1], vel[0], vel[1]))

    christmas = False
    seconds = 0
    while not christmas:
        seconds += 1
        points = set()
        for robot in robots:
            robot.x = (robot.x + robot.vel_x) % max_x
            robot.y = (robot.y + robot.vel_y) % max_y
            points.add((robot.x, robot.y))
        for y in range(max_y):
            for x in range(max_x):
                if (x, y) in points:
                    print("x ", end="")
                else:
                    print(". ", end="")
            print("")
        ans = input(f"is it christmas {seconds} ? ")
        if ans == "y":
            christmas = True
    print(seconds)


def wrapper():
    test = False
    ext = "test" if test else ""

    with open(f"./data/{Path(__file__).stem}{ext}")as f:
        data = f.readlines()
    data = [x.rstrip() for x in data]

    do2(data, test)


if __name__ == '__main__':
    wrapper()
