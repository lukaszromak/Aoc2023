import os

DIRECTIONS = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1)
}


def find_start(grid):
    for idx, row in enumerate(grid):
        for c_idx, char in enumerate(row):
            if char == "S":
                return (idx, c_idx)
           
    return None


def area_of(grid, start, steps):
    next_moves = set(start)

    for _ in range(steps):
        moves = next_moves
        next_moves = set()
        for move in moves:
            x, y = move
            for direction, movs in DIRECTIONS.items():
                mov_x, mov_y = movs
                if x + mov_x >= len(grid) or x + mov_x < 0:
                    continue
                if y + mov_y >= len(grid[y]) or y + mov_y < 0:
                    continue
                if direction == "N":
                    if grid[x + mov_x][y] == ".":
                        next_moves.add((x + mov_x, y))
                if direction == "S":
                    if grid[x + mov_x][y] == ".":
                        next_moves.add((x + mov_x, y))
                if direction == "E":
                    if grid[x][y + mov_y] == ".":
                        next_moves.add((x, y + mov_y))
                if direction == "W":
                    if grid[x][y + mov_y] == ".":
                        next_moves.add((x, y + mov_y))            
      

    return set(next_moves)    


def part2(grid, num_steps):
    #get rid of start
    start = find_start(grid)
    grid[start[0]][start[1]] = "."

    #most west fragment
    w_area = area_of(grid, [(int((len(grid) / 2)), len(grid) - 1)], 130)

    #most north fragment
    n_area = area_of(grid, [(0, int((len(grid) / 2)))], 130)

    #most east fragment
    e_area = area_of(grid, [(int((len(grid) / 2)), 0)], 130)

    #most south fragment
    s_area = area_of(grid, [(len(grid) - 1, int((len(grid) / 2)))], 130)

    #small west-north fragment
    small_wn_fragment_steps = len(grid) - min([x[1] for x in w_area if x[0] == 0]) -2
    s_wn_area = area_of(grid, [(len(grid) - 1, len(grid) - 1)], small_wn_fragment_steps)

    #small east-north fragment
    small_en_fragment_steps = len(grid) - max([x[1] for x in e_area if x[0] == 0]) - 2
    s_en_area = area_of(grid, [(len(grid) -1, 0)], small_en_fragment_steps)

    #small west-south fragment
    small_ws_fragment_steps = len(grid) - min([x[1] for x in w_area if x[0] == len(grid) - 1]) - 2
    s_ws_area = area_of(grid, [(0, len(grid) - 1)], small_ws_fragment_steps)

    #small east-south fragment
    small_es_fragment_steps = len(grid) - max(x[1] for x in e_area if x[0] == len(grid) - 1) - 2
    s_es_area = area_of(grid, [(0, 0)], small_es_fragment_steps)

    #big east-north fragment
    b_en_fragment_steps = len(grid) - min([x[1] for x in s_wn_area if x[0] == len(grid) - 1])
    b_en_area = area_of(grid, [(len(grid) - 1, len(grid) -1)], 130 + b_en_fragment_steps)
    
    #big west-north fragment
    b_wn_fragment_steps = len(grid) - max([x[1] for x in s_en_area if x[0] == len(grid) - 1]) - 2
    b_wn_area = area_of(grid, [(len(grid) - 1, 0)], 130 + b_wn_fragment_steps)

    #big east-south fragment
    b_es_area_steps = len(grid) - max(x[1] for x in s_es_area if x[0] == 0) - 2
    b_es_area = area_of(grid, [(0, 0)], 130 + b_es_area_steps)

    #big west-south
    b_ws_area_steps = len(grid) - min(x[1] for x in s_ws_area if x[0] == 0)
    b_ws_area = area_of(grid, [(0, len(grid) - 1)], 130 + b_ws_area_steps)

    radius = int((num_steps - 65) / 131)
    return (radius ** 2) * 7780 + ((radius - 1)  ** 2) * 7769 + radius * len(s_en_area) + radius * len(s_es_area) + radius * len(s_wn_area) + radius * len(s_ws_area) + (radius - 1) * len(b_en_area) + (radius - 1) * len(b_es_area) + (radius - 1) * len(b_wn_area) + (radius - 1) * len(b_ws_area) + len(n_area) + len(w_area) + len(s_area) + len(e_area)


with open("input.txt") as file:
    lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    print(part2(grid, 26501365))

