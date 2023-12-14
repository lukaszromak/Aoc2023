import math

def find_lines(rocks, grid):
    horizontal_lines = []

    for i in range(len(grid) - 1):
        horizontal_pos = i + 0.5
        for j in range(1, int(len(grid) / 2) + 1):
            if horizontal_pos - j > -1 and horizontal_pos + j < len(grid):
                horizontal_lines.append([(horizontal_pos, j), [rock for rock in rocks if abs(rock[0] - horizontal_pos) < j]])
    
    return horizontal_lines


def is_smudge(row1, row2):
    if abs(len(row1) - len(row2)) == 1:
        if len(row1) > len(row2):
            longer_row = row1
            shorter_row = row2
        else:
            longer_row = row2
            shorter_row = row1
        count_same_pos = len([x for x in longer_row if x in shorter_row])
        if count_same_pos == len(shorter_row):
            return True
    return False


def compare_rows(row1, row2, findSmudge):
    # returns equal, equal with smudge
    if row1 == row2:
        return True, False
    if findSmudge and is_smudge(row1, row2):
        return False, True
    return False, False


def find_reflections(rocks, grid, findSmudge):
    horizontal_lines = find_lines(rocks, grid)

    reflections = {}
    for horizontal_line in horizontal_lines:
        smudge = False
        reflection = True
        line, in_line = horizontal_line
        line_num, line_height = line
        above = [x for x in in_line if x[0] < line_num]
        below = [x for x in in_line if x[0] > line_num]

        for i in range(1, line_height + 1):
            row_above_y = list([x[1] for x in above if x[0] == int(math.ceil(line_num - i))])
            row_below_y = list([x[1] for x in below if x[0] == int(math.floor(line_num + i))])
            equal, isSmudge = compare_rows(row_above_y, row_below_y, findSmudge)
            if not equal:
                if isSmudge:
                    smudge = True
                    continue
                reflection = False
                break

        if reflection and (line_num + i > len(grid) - 1 or line_num - i < 0):
            if findSmudge and smudge:
                reflections[line_num] = i
            elif not findSmudge:
                reflections[line_num] = i

    return reflections


def get_rocks(grid):
    rocks = []
    for idx, line in enumerate(grid):
        for c_idx, char in enumerate(line):
            if char == "#":
                rocks.append((idx, c_idx))
    return rocks


def solve(grids, findSmudge):
    count = 0
    for grid in grids:
        # horizontal
        rocks = get_rocks(grid)
        reflections = find_reflections(rocks, grid, findSmudge)
        count += sum([math.ceil(x) * 100 for x in reflections.keys()])
        #vertical
        grid_rotate = list(zip(*grid[::-1]))
        rocks = get_rocks(grid_rotate)
        reflections = find_reflections(rocks, grid_rotate, findSmudge)
        count += sum([math.ceil(x) for x in reflections.keys()])   
    return count


with open("input.txt") as file:
    lines = file.read().split("\n\n")
    grids = [[list(y) for y in x.split("\n")] for x in lines]

print("pt1:", solve(grids, False))
print("pt2:", solve(grids, True))