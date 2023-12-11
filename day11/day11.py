def taxicab_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def get_pairs(lines, spread):
    matrix = []
    for line in lines:
        if line.count("#") == 0:
            matrix.append(spread)
        else:
            matrix.append([*line])
    
    matrix = matrix[::-1]
    x_size = len(matrix[0])
    y_size = len(matrix)

    tmp = []
    for i in range(x_size):
        values = []
        is_empty = True
        for j in range(y_size):
            if type(matrix[j]) == int:
                val = matrix[j]
            else:
                val = matrix[j][i]
            if type(val) != int and val != ".":
                is_empty = False
            values.append(val)
        if is_empty:
            tmp.append([spread] * y_size)
        else:
            tmp.append(values)

    matrix = tmp
    galaxies = []
    x_distance = 0
    y_distance = 0
    for i in range(len(matrix)):
        if type(matrix[i][0]) == int:
            x_distance += matrix[i][j]
            continue
        y_distance = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == "#":
                galaxies.append((x_distance, y_distance))
            if(type(matrix[i][j])) == int:
                y_distance += matrix[i][j]
            else:
                y_distance += 1
        x_distance += 1
    
    return list([(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]])


with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

    pairs = get_pairs(lines, 2)
    print("part1:", sum([taxicab_distance(pair[0], pair[1]) for pair in pairs]))
    pairs = get_pairs(lines, 1000000)
    print("part2:", sum([taxicab_distance(pair[0], pair[1]) for pair in pairs]))