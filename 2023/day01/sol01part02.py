import os
import re

def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines

def sol01part02():
    lines = read_input()

    _sum = 0
    str_digits = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
    r = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))") # (?=...) is needed for cases like "eightwo"

    for line in lines:
        digits = r.findall(line)

        for i in [0, -1]:
            if digits[i] in str_digits:
                digits[i] = str_digits[digits[i]]

        _sum += int(digits[0] + digits[-1])
    

    return _sum


if __name__ == "__main__":
    sol = sol01part02()
    print(sol)
