import os
import re


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def sol01part02():
    lines = read_input()

    r = re.compile(r"(\d)")
    time = int(''.join(r.findall(lines[0])))
    distance = int(''.join(r.findall(lines[1])))

    for i in range(time): # TODO: we can optimize this via binary search
        if i * (time - i) > distance:
            break

    return abs(time - 2 * i) + 1


if __name__ == "__main__":
    sol = sol01part02()
    print(sol)
