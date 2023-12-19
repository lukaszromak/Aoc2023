from PIL import Image
import copy
import os

# offset for visualization
START_OFFSET = 10

# create points in cartesian coordinate system, starting from [0, 0]
def create_points(dig_plan):
    DIRECTIONS = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }
    x, y = 0, 0
    points = [[x, y]]

    for trench in dig_plan:
        direction, length, hex = trench
        movement = DIRECTIONS[direction]
        x += movement[0] * int(length)
        y += movement[1] * int(length)
        points.append([x, y])

    return points


def create_points_hex(dig_plan):
    HEX_DIRECTIONS = {
        0: (1, 0),
        1: (0, -1),  
        2: (-1, 0),
        3: (0, 1),  
    }
    x, y = 0, 0
    points = [[x, y]]

    for trench in dig_plan:
        d, l, hex = trench
        length = int(hex[2:-2], 16)
        movement = HEX_DIRECTIONS[int(hex[-2])]
        x += movement[0] * length
        y += movement[1] * length
        points.append([x, y])
    
    return points

# move cartesian coordinate system points (+,+) quadrant 
def move_points(_points):
    points = copy.deepcopy(_points)
    lowest_x = min(points, key=lambda x: x[0])[0]
    lowest_y = min(points, key=lambda x: x[1])[1]

    if lowest_x == 0:
        move_x = START_OFFSET
    elif lowest_x > 0:
        move_x = -lowest_x - START_OFFSET
    else:
        move_x = abs(lowest_x) + START_OFFSET

    if lowest_y == 0:
        move_y = START_OFFSET
    elif lowest_y > 0:
        move_y = -lowest_y - START_OFFSET
    else:
        move_y = abs(lowest_y) + START_OFFSET

    for i in range(len(points)):
        x, y = points[i]
        points[i] = [x + move_x, y + move_y]

    return points


#creates grid with size based on furthest cartestian coordinate system points
def create_grid(points):
    highest_x = max(points, key=lambda x: x[0])[0]
    highest_y = max(points, key=lambda x: x[1])[1]

    grid = [["."] * (highest_x + START_OFFSET)] * (abs(highest_y) + START_OFFSET)

    return grid


#fills grid, by going from point to point
def fill_grid(_grid, points):
    grid = copy.deepcopy(_grid)

    for i in range(1, len(points)):
        prev_x, prev_y = points[i - 1]
        curr_x, curr_y = points[i]

        if prev_y == curr_y:
            idx_from = min(prev_x, curr_x)
            idx_to = max(prev_x, curr_x)
            grid[prev_y] = grid[prev_y][:idx_from] + (["#"] * (idx_to - idx_from + 1)) + grid[prev_y][idx_to + 1:]
        elif prev_x == curr_x:
            idx_from = min(prev_y, curr_y)
            idx_to = max(prev_y, curr_y)
            for i in range(idx_from, idx_to):
                grid[i] = grid[i][:prev_x] + ["#"] + grid[i][prev_x + 1:]

    return grid


#creates image based on grid
def create_image(grid):
    width = len(grid[0])
    height = len(grid)
    image = Image.new("RGB", (width, height), (255, 255, 255))

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            color = (0, 0, 0) if value == "#" else (255, 255, 255)
            image.putpixel((x, y), color)

    image.save("output_image.png")


def find_cubic_meters(points):
    num_integer_points = 0
    col1 = []
    col2 = []

    for idx, point in enumerate(points[:-1]):
        num_integer_points += abs(point[0] - points[idx + 1][0]) + abs(point[1] - points[idx + 1][1])
        col1.append(point[0] * points[idx + 1][1])
        col2.append(point[1] * points[idx + 1][0])

    #area calculated using shoelace method
    area = int(abs(sum(col1) - sum(col2)) / 2)

    #num of interior points using pick's theorem + boundary points
    return int(area - num_integer_points/2 + 1) + num_integer_points

        
with open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt") as file:
    dig_plan = [tuple(line.strip().split()) for line in file.readlines()]

# pt 1
points = create_points(dig_plan)
points = move_points(points)
print("part1:", find_cubic_meters(points))
# visualization 
grid = create_grid(points)
grid = fill_grid(grid, points)
create_image(grid)

# pt 2
points = create_points_hex(dig_plan)
points = move_points(points)
print("part2:", find_cubic_meters(points))
