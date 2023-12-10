from termcolor import colored

with open("input.txt") as file:
    lines = file.readlines()
    grid = []
    start = (0, 0)
    for idx, line in enumerate(lines):
        grid.append(line)
        if line.count("S") == 1:
            start = (idx, line.index("S"))

    pipes = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": [(0, 0)]
    }

    loop = []
    for pipe in pipes.keys():
        x, y = start
        grid[x] = grid[x][:y] + pipe + grid[x][y + 1:]
        current_pos = (x, y)
        visited = []
        prev_pos = start
        loop_found = False

        while current_pos not in visited:
            visited.append(current_pos)
            x, y = current_pos

            for movement in pipes[grid[x][y]]:
                conn = False
                mov_x, mov_y = movement
                if (x + mov_x, y + mov_y) not in visited:
                    # check if next pipe is connected to the current one
                    next_movements = pipes[grid[x + mov_x][y + mov_y]]
                    for next_movement in next_movements:
                        if mov_x + next_movement[0] == 0 and mov_y + next_movement[1] == 0:
                            prev_pos = current_pos
                            current_pos = (x + mov_x, y + mov_y)
                            conn = True
                    if conn:
                        break
                elif (x + mov_x, y + mov_y) in visited:
                    if x + mov_x == start[0] and y + mov_y == start[1]:
                        # check if start is connected to current pipe
                        next_movements = pipes[grid[x + mov_x][y + mov_y]]
                        for next_movement in next_movements:
                            if mov_x + next_movement[0] == 0 and mov_y + next_movement[1] == 0 and prev_pos != start:
                                loop = visited
                                loop_found = True
                                break      
        if loop_found:
            break 

    

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in loop:
                print(colored(grid[i][j], "red"), end="")
            else:
                print(grid[i][j], end="")
        print(end="")
    print()

    print("part1:", len(loop) / 2)