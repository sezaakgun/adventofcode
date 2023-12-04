from collections import defaultdict
import os


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def get_score(body):
    winners, numbers = map(lambda x: set(x.split(' ')), body.replace('  ', ' ').split(' | '))
    return len(numbers.intersection(winners))


def sol01part02():
    lines = read_input()
    count = 0
    multiplier = defaultdict(lambda: 1)
    for line in lines:
        card_info, body = line.split(': ')
        card_id = int(card_info.split(' ')[-1])
        score = get_score(body)
        current_multiplier = max(multiplier[card_id], 1)
        count += current_multiplier

        for i in range(score):
            multiplier[card_id + i + 1] += current_multiplier

    return count


if __name__ == "__main__":
    sol = sol01part02()
    print(sol)
