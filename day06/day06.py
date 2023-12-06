import functools

def count_ways_to_beat_record(time, distance_to_beat):
    time = int(time)
    distance_to_beat = int(distance_to_beat)

    counter = 0
    for i in range(time):
         distance_travelled = (time - i) * i
         if distance_travelled > distance_to_beat:
              counter += 1

    return counter

with open("input.txt") as file:
    times, distances = [x.strip().split()[1:] for x in file.readlines()]
    
    print("pt1: ", functools.reduce(lambda x, y: x * y, [count_ways_to_beat_record(time, distances[i]) for i, time in enumerate(times)]))
    print("pt2: ", count_ways_to_beat_record("".join(times), "".join(distances)))