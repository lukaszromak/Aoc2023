def parse_input(lines):
    hailstones = []

    for line in lines:
        position, velocity = line.split(" @ ")
        hailstones.append([[int(x) for x in position.split(", ")], [int(x) for x in velocity.split(", ")]])

    return hailstones


def hailstones_to_lines(hailstones):
    lines = []

    for hailstone in hailstones:
        p1_x, p1_y = hailstone[0][0], hailstone[0][1]
        p2_x, p2_y = hailstone[0][0] + hailstone[1][0], hailstone[0][1] + hailstone[1][1]

        if p2_x > p1_x:
            x_direction = "E"
        else:
            x_direction = "W"

        if p2_y > p1_y:
            y_direction = "N"
        else:
            y_direction = "S"

        a = (p1_y - p2_y) / (p1_x - p2_x)
        b = p1_y - ((p1_y - p2_y) / (p1_x - p2_x) * p1_x)
        lines.append((((a, b), (x_direction, y_direction), (p1_x, p1_y))))

    return lines


def find_intersections(lines, min, max):
    count = 0

    for idx, line in enumerate(lines):
        for line2 in lines[idx + 1:]:
            func_1, dir_1, start_1 = line
            func_2, dir_2, start_2 = line2
            a, c = func_1
            b, d = func_2
            
            if a == b:
                continue

            x = (d - c) / (a - b)
            y = a * ((d - c) / (a - b)) + c

            if x < min or x > max:
                continue

            if y < min or y > max:
                continue

            if (dir_1[0] == "E" and x < start_1[0]) or (dir_1[0] == "W" and x > start_1[0]):
                continue

            if (dir_2[0] == "E" and x < start_2[0]) or (dir_2[0] == "W" and x > start_2[0]):
                continue

            if (dir_1[1] == "N" and y < start_1[1]) or (dir_1[1] == "S" and y > start_1[1]):
                continue

            if (dir_2[1] == "N" and y < start_2[1]) or (dir_2[1] == "S" and y > start_2[1]):
                continue

            count += 1

    return count


with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    hailstones = parse_input(lines)
    lines = hailstones_to_lines(hailstones)

    MIN = 200000000000000
    MAX = 400000000000000

    print("part1:", find_intersections(lines, MIN, MAX))
