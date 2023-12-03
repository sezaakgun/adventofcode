import os


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def check_neighbours(x, y, lines):
    last_number = 0 # easy way to check if we have already seen this number
    _sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if 0 <= x + i < len(lines) and 0 <= y + j < len(lines[0]):
                number = find_numbers(x + i, y + j, lines)
                if last_number != number:
                    last_number = number
                    _sum += number

    return _sum


def find_numbers(x, y, lines):
    if lines[x][y] == '.':
        return 0
    
    line = lines[x]
    number = ""
    curr = y
    while line[curr].isdigit():
        number = number + line[curr]
        curr += 1
        if curr >= len(line):
            break
    
    curr = y - 1
    while line[curr].isdigit():
        number = line[curr] + number
        curr += -1
        if curr < 0:
            break
        
    return int(number)


def sol01part01():
    lines = read_input()
    symbols = {'*', '@', '#', '$', '%', '&', '=', '/', '+', '-'}
    _sum = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char in symbols:
                neighbour_sum = check_neighbours(x, y, lines)
                _sum += neighbour_sum
                print(neighbour_sum)
                

    return _sum


if __name__ == "__main__":
    sol = sol01part01()
    print(sol)
