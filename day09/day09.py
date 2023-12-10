def extrapolated_sum(squences):
    count = 0
    for sequence in sequences:
        subsequences = [sequence]
        prev_sequence = sequence
        while not prev_sequence.count(0) == len(prev_sequence):
            tmp = []
            for i in range(1, len(prev_sequence)):
                tmp.append(prev_sequence[i] - prev_sequence[i - 1])
            subsequences.append(tmp)
            prev_sequence = tmp

        for i in range(1, len(subsequences)):
            subsequences[i].append(subsequences[i - 1][-1] + subsequences[i][-1])
        count += subsequences[-1][-1]

        subsequences = []
    return count

with open("input.txt") as file:
    lines = file.readlines()
    sequences = [[int(y) for y in x.strip().split(" ")] for x in lines]
    print("part1:", extrapolated_sum(sequences))
    sequences = [[int(y) for y in list(reversed(x.strip().split(" ")))] for x in lines]
    print("part2:", extrapolated_sum(sequences))
