import os


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def sol01part01():
    lines = read_input()

    seeds = map(int, lines[0].split(" ")[1:])
    min_location = float('inf')

    for seed in seeds:
        transit_val = seed
        found = False
        for line in lines[3:]:
            if found and line != "":
                continue

            if line == "":
                found = False
                continue
            
            if "map" in line:
                continue
            
            source, destination, size = map(int, line.split(" "))
            if transit_val >= destination and transit_val < destination + size:
                transit_val = source + (transit_val - destination)
                found = True
        
        min_location = min(min_location, transit_val)

    return min_location


if __name__ == "__main__":
    sol = sol01part01()
    print(sol)
