import os
import time
import multiprocessing


def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines


def sol01part02():
    lines = read_input()

    seeds = list(map(int, lines[0].split(" ")[1:]))
    min_location = float('inf')
    min_locations = []

    outer_maps = []
    inner_maps = []

    for line in lines[3:]:
        if line == "":
            outer_maps.append(inner_maps)
            inner_maps = []
            continue
        
        if "map" in line:
            continue
        
        inner_maps.append(list(map(int, line.split(" "))))
    else:
        outer_maps.append(inner_maps)

    args = [(seeds[i], seeds[i+1], outer_maps, i) for i in range(0, len(seeds), 2)]

    # Create a Pool object and use it to apply the function to the arguments
    with multiprocessing.Pool() as pool:
        results = pool.map(process_seed_range, args)

    return min(results)


def process_seed_range(args):
    t = time.time()
    seed_start, seed_range, outer_maps, i = args
    min_location = float('inf')
    for seed in range(seed_start, seed_start+seed_range):
        transit_val = seed
        for inner_maps in outer_maps:
            for (source, destination, size) in inner_maps:
                if transit_val >= destination and transit_val < destination + size:
                    transit_val = source + (transit_val - destination)
                    break
        min_location = min(min_location, transit_val)
    print(f"Process {i} taken: ", time.time() - t)
    return min_location


if __name__ == "__main__":
    sol = sol01part02()
    print(sol)
