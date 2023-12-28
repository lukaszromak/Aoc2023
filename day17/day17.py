import os
from queue import PriorityQueue

DIRECTIONS = {
    "U": (-1, 0), 
    "D": (1, 0), 
    "L": (0, -1),
    "R": (0, 1)
}

FORBIDDEN_TURNS = {
    "U": "D",
    "D": "U", 
    "L": "R",
    "R": "L"
}


def dijkstra(grid, target, min_steps, max_steps):
    start_1 = (0, min_steps - 1, min_steps, "R")
    start_2 = (min_steps -1, 0, min_steps, "D")
    dist = {}
    dist[start_1] = sum(grid[0][1:min_steps])
    dist[start_2] = sum(x[0] for x in grid[1:min_steps])

    pq = PriorityQueue()
    pq.put((dist[start_1], *start_1))
    pq.put((dist[start_2], *start_2))

    while not pq.empty():
        heatloss, curr_x, curr_y, steps, direction = pq.get()

        for dir_name, movs in DIRECTIONS.items():
            x, y = curr_x, curr_y
            alt = heatloss
            mov_x, mov_y = movs
            nsteps = min_steps

            if dir_name == direction:
                if steps + 1 <= max_steps:
                    nsteps = steps + 1
                    x += mov_x
                    y += mov_y
                else:
                    continue
            else:
                x += mov_x * min_steps
                y += mov_y * min_steps
            
            if FORBIDDEN_TURNS[direction] == dir_name:
                continue

            if x < 0 or x >= len(grid):
                continue

            if y < 0 or y >= len(grid[x]):
                continue

            if nsteps == min_steps:
                for i in range(1, nsteps + 1):
                    alt += grid[curr_x + mov_x * i][curr_y + mov_y * i]
            else:
                alt += grid[x][y]

            if (x, y, nsteps, dir_name) not in dist or alt < dist[(x, y, nsteps, dir_name)]:
                dist[(x, y, nsteps, dir_name)] = alt
                pq.put((alt, x, y, nsteps, dir_name))

    paths_to_target = [(node, dist[node]) for node in dist.keys() if node[0] == target[0] and node[1] == target[1]]
    return min(paths_to_target, key=lambda x: x[1])[1]       


with open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt") as file:
    lines = file.readlines()
    grid = [[int(y) for y in list(line.strip())] for line in lines]
    target = (len(grid) - 1, len(grid[len(grid) - 1]) - 1)

    print("part1:", dijkstra(grid, target, 1, 3))    
    print("part2:", dijkstra(grid, target, 4, 10)) 