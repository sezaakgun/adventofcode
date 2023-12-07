import os


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def sol01part02():
    lines = read_input()
    return lines


if __name__ == "__main__":
    sol = sol01part02()
    print(sol)
