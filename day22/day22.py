from queue import PriorityQueue
import copy
import os

def fall(falling, bricks):
    if falling[0][2] == 1:
        return 0, []
    
    stopped_on = []
    z_start = falling[0][2]   
    z_fallen = 0

    while True:
        for brick in bricks:
            if brick[1][2] == z_start - 1:
                if falling[1][0] < brick[0][0] or falling[0][0] > brick[1][0]:
                    continue
                if falling[1][1] < brick[0][1] or falling[0][1] > brick[1][1]:
                    continue
                stopped_on.append(tuple([tuple(brick[0]), tuple(brick[1])]))
        if len(stopped_on) > 0 or z_start == 1:
            break
        z_fallen += -1
        z_start += -1

    return z_fallen, stopped_on


def move_bricks(_bricks):
    bricks = copy.deepcopy(_bricks)
    standing_on = {}

    for i in range(len(bricks)):
        z_fallen, stopped_on = fall(bricks[i], bricks)
        bricks[i][0][2] += z_fallen
        bricks[i][1][2] += z_fallen
        standing_on[(tuple(bricks[i][0]), tuple(bricks[i][1]))] = stopped_on

    return standing_on


def how_many_would_fall(brick, standing_on):
    dependencies = PriorityQueue(maxsize=100000)
    dependencies.put((brick[1][0], brick))
    dependency_chain = set()

    while not dependencies.empty():
        _, next = dependencies.get()

        if next in dependency_chain:
            continue

        dependency_chain.add(next)

        for brick in standing_on:
            if next in standing_on[brick] and set(standing_on[brick]).intersection(dependency_chain) == set(standing_on[brick]):
                dependencies.put((brick[0][2], brick))

    return len(dependency_chain) - 1


def disintegrate(standing_on):
    count_pt1 = len(standing_on)
    count_pt2 = 0

    for b1 in standing_on:
        for b2 in standing_on:
            if b1 in standing_on[b2] and len(standing_on[b2]) == 1:
                count_pt1 += -1
                count_pt2 += how_many_would_fall(b1, standing_on)
                break
    
    return count_pt1, count_pt2


with open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt") as file:
    lines = file.readlines()

    bricks = []
    for line in lines:
        start = [int(x) for x in line.split("~")[0].split(",")]
        end = [int(x) for x in line.split("~")[1].split(",")]
        bricks.append([start, end])

    bricks = sorted(bricks, key=lambda x: x[0][2])
    standing_on = move_bricks(bricks)
    pt_1, pt_2 = disintegrate(standing_on)
    print("part1:", pt_1)
    print("part2:", pt_2)
