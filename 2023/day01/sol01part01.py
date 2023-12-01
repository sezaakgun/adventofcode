import os
import re

def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.readlines()
    return lines

def sol01part01():
    lines = read_input()

    _sum = 0
    r = re.compile(r"\d")

    for line in lines:
        digits = r.findall(line)
        _sum += int(digits[0] + digits[-1])

    return _sum

if __name__ == "__main__":
    sol = sol01part01()
    print(sol)
