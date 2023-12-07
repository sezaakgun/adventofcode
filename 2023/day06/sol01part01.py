import os
import re


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def sol01part01():
    lines = read_input()
    _mul = 1

    r = re.compile(r"(\d+)")
    times = map(int, r.findall(lines[0]))
    distances = map(int, r.findall(lines[1]))

    for (time, distance) in zip(times, distances):
        for i in range(time): # TODO: we can optimize this via binary search
            if i * (time - i) > distance:
                break
        _mul *= abs(time - 2 * i) + 1

    return _mul


if __name__ == "__main__":
    sol = sol01part01()
    print(sol)
