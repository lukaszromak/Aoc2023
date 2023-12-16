import os
import copy

def energized_tiles(_grid, start_pos):
    grid = copy.deepcopy(_grid)
    translations = {
    (0, 1, "/"): (-1, 0),
    (-1, 0, "/"): (0, 1),
    (0, -1, "/"): (1, 0),
    (1, 0, "/"): (0, -1),    
    (0, 1, "\\"): (1, 0),
    (-1, 0, "\\"): (0, -1),
    (0, -1, "\\"): (-1, 0),
    (1, 0, "\\"): (0, 1)
    }

    beams = set()
    queue = [start_pos]
    while queue:
        curr_beam = queue.pop(0)
        x, y = curr_beam[0]
        mov_x = curr_beam[1]
        mov_y = curr_beam[2]

        while True:
            beams.add((x, y))
            if grid[x][y] == ".":
                grid[x][y] = [(mov_x, mov_y)]
            elif type(grid[x][y]) == list:
                same_beam = [beam for beam in grid[x][y] if beam == (mov_x, mov_y)]
                if len(same_beam) > 0:
                    break
                grid[x][y].append((mov_x, mov_y))
            elif grid[x][y] == "/":
                mov_x, mov_y = translations[(mov_x, mov_y, "/")]
            elif grid[x][y] == "\\":
                mov_x, mov_y = translations[(mov_x, mov_y, "\\")]
            elif grid[x][y] == "-":
                if mov_y == 0:
                    if y + 1 < len(grid[0]):
                        queue.append(((x, y + 1), 0, 1))
                    if y - 1 >= 0:
                        queue.append(((x, y - 1), 0, -1))
                    break
            elif grid[x][y] == "|":
                if mov_x == 0:
                    if x + 1 < len(grid):
                        queue.append(((x + 1, y), 1, 0))
                    if x - 1 >= 0:
                        queue.append(((x - 1, y), -1, 0))
                    break
            x += mov_x
            y += mov_y
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                break

    return len(beams)


def max_energized_grid(grid):
    max = 0

    #top row
    for i in range(len(grid[0])):
        num_energized_tiles = energized_tiles(grid, ((0, i), 1, 0))
        if num_energized_tiles > max:
            max = num_energized_tiles
    
    #bottom row
    for i in range(len(grid[0])):
        num_energized_tiles = energized_tiles(grid, ((len(grid) - 1, i), -1, 0))
        if num_energized_tiles > max:
            max = num_energized_tiles

    #leftmost column
    for i in range(len(grid)):
        num_energized_tiles = energized_tiles(grid, ((i, 0), 0, 1))
        if num_energized_tiles > max:
            max = num_energized_tiles        

    #rightmost column
    for i in range(len(grid)):
        num_energized_tiles = energized_tiles(grid, ((i, len(grid) - 1), 0, -1))
        if num_energized_tiles > max:
            max = num_energized_tiles       

    return max


with open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt") as file:
    grid = [list(line.strip()) for line in file.readlines()]

print("part1:", energized_tiles(grid, ((0, 0), 0, 1)))
print("part2:", max_energized_grid(grid))