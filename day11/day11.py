def taxicab_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def get_pairs(lines, spread):
    matrix = []
    for line in lines:
        if line.count("#") == 0:
            for i in range(spread):
                matrix.append(line)
        else:
            matrix.append([*line])

    matrix = list(zip(*matrix[::-1]))

    galaxies = []
    tmp = []
    for i, row in enumerate(matrix):        
        if row.count("#") == 0:
            for i in range(spread):
                tmp.append(row)
        else:
            tmp.append(row)

    matrix = tmp
    for i, row in enumerate(matrix):        
        if row.count("#") > 0:
            for j, char in enumerate(row):
                if char == "#":
                    galaxies.append((i, j))

    pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    return pairs

with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

    pairs = get_pairs(lines, 2)
    print(sum([taxicab_distance(pair[0], pair[1]) for pair in pairs]))