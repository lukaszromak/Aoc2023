with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    instructions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        nodes[lines[i].split(" = ")[0]] = lines[i].split(" = ")[1][1:-1].split(", ")

    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current_node = nodes[current_node][0]
            elif instruction == "R":
                current_node = nodes[current_node][1]
            steps += 1
    print(steps)