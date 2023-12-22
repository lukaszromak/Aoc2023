import os

def find_start(grid):
    for idx, row in enumerate(grid):
        for c_idx, char in enumerate(row):
            if char == "S":
                return (idx, c_idx)
            
    return None


def print_grid(grid, moves):
    os.system("cls")
    for idx, row in enumerate(grid):
        for c_idx, char in enumerate(row):
            if (idx, c_idx) in moves:
                print("O", end="")
            else:
                print(char, end="")
        print()
    input()


def perform_step(grid, moves):
    DIRECTIONS = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1)
    }
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
            
    return next_moves


def perform_steps(grid, num_steps):
    moves = [find_start(grid)]
    start_x, start_y = moves[0]
    grid[start_x][start_y] = "."

    for _ in range(num_steps):
        moves = perform_step(grid, moves)
    
    return len(set(moves))       

with open("input.txt") as file:
    grid = [list(line.strip()) for line in file.readlines()]
    print("part1:", perform_steps(grid, 64))