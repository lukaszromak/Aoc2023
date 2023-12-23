from queue import Queue
import copy
import os
import networkx as nx
import matplotlib.pyplot as plt

DIRECTIONS = {
    "N": (-1, 0),
    "W": (0, -1),
    "E": (0, 1),
    "S": (1, 0)
}

SLOPES = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

def visualize_graph(graph):
    positions = {}
    positions[(0, 1)] = [0, 1]
    g = nx.Graph()

    for node, adjacent in graph.items():
        positions[node] = [node[0], node[1]]
        for neighbour in adjacent:
            g.add_edge(neighbour[0], node, weight=neighbour[1])

    fig = plt.figure(1, figsize=(19, 10), dpi=300)
    nx.draw_networkx_nodes(g, positions)
    nx.draw_networkx_edges(g, positions, width=1)
    nx.draw_networkx_labels(g, positions, font_size=10, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, positions, edge_labels)
    fig.savefig("condensed_graph.png")


def traverse_paths(grid, target):
    q = Queue()
    q.put((1, 1, [(0, 1)], (0, 1), 0))
    paths = []
    condensed_graph = {}

    while not q.empty():
        x, y, path, prev_split, steps = q.get()

        if (x, y) == target:
            if (x, y) not in condensed_graph:
                condensed_graph[(x, y)] = list()
                condensed_graph[(x,y)].append((prev_split, steps))
            else:
                condensed_graph[(x, y)].append((prev_split, steps))
            paths.append(path)
            continue

        prev_split = (path[-1])
        steps = 0

        while True:
            steps += 1
            available_directions = []

            if grid[x][y] in SLOPES.keys():
                mov_x, mov_y = SLOPES[grid[x][y]]
                if (x + mov_x, y + mov_y) not in path:
                    available_directions.append((x + mov_x, y + mov_y))
            else:
                for direction in DIRECTIONS.values():
                    mov_x, mov_y = direction

                    if x + mov_x < 0 or x + mov_x >= len(grid):
                        continue

                    if y + mov_y < 0 or y + mov_y >= len(grid[y]):
                        continue

                    next = grid[x + mov_x][y + mov_y]
                    if (next == "." or next in SLOPES.keys()) and (x + mov_x, y + mov_y) not in path:
                        available_directions.append((x + mov_x, y + mov_y))


            if len(available_directions) == 1:
                path.append((x, y))
                x = available_directions[0][0]
                y = available_directions[0][1]
                continue

            if len(available_directions) == 0:
                if (x + mov_x, y + mov_y) == target:
                    q.put((x + mov_x, y + mov_y, copy.deepcopy(path), prev_split, steps))
                break

            if len(available_directions) > 1:
                path.append((x, y))
                if (x, y) not in condensed_graph:
                    condensed_graph[(x, y)] = list()
                    condensed_graph[(x,y)].append((prev_split, steps))
                else:
                    condensed_graph[(x, y)].append((prev_split, steps))
                for available_direction in available_directions:
                    x, y = available_direction
                    q.put((x, y, copy.deepcopy(path), prev_split, steps))
                break

    return condensed_graph, max([len(x) for x in paths])


def longest_path(condensed_graph, source, target):
    g = nx.Graph()
    for node, adjacent in condensed_graph.items():
        for neighbour in adjacent:
            g.add_edge(neighbour[0], node, weight=neighbour[1])

    longest_path = 0
    for path in nx.all_simple_paths(g, source, target):
        path_weight = nx.path_weight(g, path, weight="weight")
        if path_weight > longest_path:
            longest_path = path_weight

    return longest_path


with open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt") as file:
    lines = file.read()
    grid = [list(line.strip()) for line in lines.split("\n")]

    starting_point = (len(grid), len(grid) - 2)
    ending_point = (0, 1)

    condensed_graph, pt_1 = traverse_paths(grid, starting_point)
    visualize_graph(condensed_graph)
    print("part1:", pt_1)
    print("part2:", longest_path(condensed_graph, starting_point, ending_point))
