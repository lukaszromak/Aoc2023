def tilt_north(grid):
    grid_copy = grid[:]

    for i in range(len(grid_copy)):
        for j in range(len(grid_copy[i])):
            if grid_copy[i][j] == "O":
                curr_i = i
                while curr_i != 0 and grid_copy[curr_i - 1][j] != "O" and grid_copy[curr_i - 1][j] != "#":
                    grid_copy[curr_i][j] = "."
                    grid_copy[curr_i - 1][j] = "O"
                    curr_i += -1

    return grid_copy


def tilt_south(grid):
    grid_copy = grid[:]

    for i in reversed(range(len(grid_copy))):
        for j in range(len(grid_copy[i])):
            if grid_copy[i][j] == "O":
                curr_i = i
                while curr_i != len(grid_copy) - 1 and grid_copy[curr_i + 1][j] != "O" and grid_copy[curr_i + 1][j] != "#":
                    grid_copy[curr_i][j] = "."
                    grid_copy[curr_i + 1][j] = "O"
                    curr_i += 1
            
    return grid_copy


def tilt_east(grid):
    grid_copy = grid[:]

    for i in range(len(grid_copy)):
        for j in reversed(range(len(grid_copy[i]))):
            if grid_copy[i][j] == "O":
                curr_j = j
                while curr_j != len(grid_copy[i]) - 1 and grid_copy[i][curr_j + 1] != "O" and grid_copy[i][curr_j + 1] != "#":
                    grid_copy[i][curr_j] = "."
                    grid_copy[i][curr_j + 1] = "O"
                    curr_j += 1

    return grid_copy


def tilt_west(grid):
    grid_copy = grid[:]

    for i in range(len(grid_copy)):
        for j in range(len(grid_copy[i])):
            if grid_copy[i][j] == "O":
                curr_j = j
                while curr_j > 0 and grid_copy[i][curr_j - 1] != "O" and grid_copy[i][curr_j - 1] != "#":
                    grid_copy[i][curr_j] = "."
                    grid_copy[i][curr_j - 1] = "O"
                    curr_j += -1

    return grid_copy


def perform_cycles(grid, num_cycles):
    patterns = []
    grid_copy = grid[:]
    functions = [tilt_north, tilt_west, tilt_south, tilt_east]

    for i in range(0, num_cycles):
        for function in functions:
            grid_copy = function(grid)

        pattern = "".join([item for row in grid_copy for item in row])
        
        if pattern in patterns:
            start = patterns.index(pattern)
            modulo = i - start
            return perform_cycles(grid, (num_cycles - start) % modulo - 1)
        else:
            patterns.append(pattern)

    return grid_copy


def calculate_load(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                count += len(grid) - i

    return count

with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    grid = [list(line) for line in lines]

print("part1:", calculate_load(tilt_north(grid)))
print("part2:", calculate_load(perform_cycles(grid, 1000000000)))