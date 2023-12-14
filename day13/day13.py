import math

def find_reflections(rocks, grid):
    horizontal_lines = []
    for i in range(len(grid) - 1):
        horizontal_pos = i + 0.5
        for j in range(1, int(len(grid) / 2) + 1):
            if horizontal_pos - j > -1 and horizontal_pos + j < len(grid):
                horizontal_lines.append([(horizontal_pos, j), [rock for rock in rocks if abs(rock[0] - horizontal_pos) < j]])

    reflections = {}
    for horizontal_line in horizontal_lines:
        reflection = True
        line, in_line = horizontal_line
        line_num, line_height = line
        above = [x for x in in_line if x[0] < line_num]
        below = [x for x in in_line if x[0] > line_num]

        for i in range(1, line_height + 1):
            row_above_y = set([x[1] for x in above if x[0] == int(math.ceil(line_num - i))])
            row_below_y = set([x[1] for x in below if x[0] == int(math.floor(line_num + i))])
            if row_above_y != row_below_y:
                reflection = False
                break
        if reflection and (line_num + i > len(grid) - 1 or line_num - i < 0):
            reflections[line_num] = i
    return reflections


def get_rocks(grid):
    rocks = []
    for idx, line in enumerate(grid):
        for c_idx, char in enumerate(line):
            if char == "#":
                rocks.append((idx, c_idx))
    return rocks


with open("input.txt") as file:
    lines = file.read().split("\n\n")
    grids = [[list(y) for y in x.split("\n")] for x in lines]

count = 0
for grid in grids:
    # horizontal
    rocks = get_rocks(grid)
    reflections = find_reflections(rocks, grid)
    print(reflections)
    count += sum([math.ceil(x) * 100 for x in reflections.keys()])
    # vertical
    grid_rotate = list(zip(*grid[::-1]))
    rocks = get_rocks(grid_rotate)
    reflections = find_reflections(rocks, grid_rotate)
    count += sum([math.ceil(x) for x in reflections.keys()])
    print(reflections)

print(count)