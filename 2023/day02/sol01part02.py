import os
from sol01part01 import fetch_statistics

def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def sol01part02():
    lines = read_input()
    game_power_sum = 0

    for statistics in fetch_statistics(lines).values():
        game_power = 1

        for count in statistics.values():
            game_power *= count
        
        game_power_sum += game_power
    
    return game_power_sum


if __name__ == "__main__":
    sol = sol01part02()
    print(sol)
