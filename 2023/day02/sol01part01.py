import os

def read_input():
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        lines = f.read().splitlines()
    return lines

def fetch_statistics(lines):
    game_stats = {}
    for line in lines:
        game_id, game_info = line.split(': ')
        for _set in game_info.split('; '):
            set_stats = {}
            for reveal in _set.split(', '):
                count, color = reveal.split(' ')
                set_stats[color] = max(set_stats.get(color, 0), int(count))
            
            key = int(game_id.split(' ')[1])
            game_stats[key] = game_stats.get(key, set_stats)
            game_stat = game_stats[key]

            for color, count in set_stats.items():
                game_stat[color] = max(game_stat.get(color, count), count)
    
    return game_stats

def sol01part01():
    lines = read_input()
    game_id_sum = 0
    constraints = {'red': 12, 'green': 13, 'blue': 14}

    for game_id, statistics in fetch_statistics(lines).items():
        satisfied = True
        for color, count in statistics.items():
            if count > constraints[color]:
                satisfied = False
        
        if satisfied:
            game_id_sum += game_id
    
    return game_id_sum

if __name__ == "__main__":
    sol = sol01part01()
    print(sol)
