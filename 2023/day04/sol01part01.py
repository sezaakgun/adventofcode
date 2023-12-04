import os


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def sol01part01():
    lines = read_input()
    _sum = 0
    for line in lines:
        _, body = line.split(': ')
        winners, numbers = map(lambda x: set(x.split(' ')), body.replace('  ', ' ').split(' | '))
        score = len(numbers.intersection(winners))
        if score != 0:
            _sum += 2**(score - 1)
    return _sum


if __name__ == "__main__":
    sol = sol01part01()
    print(sol)
