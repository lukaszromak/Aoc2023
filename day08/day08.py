def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(numbers):
    if len(numbers) < 2:
        return None
    if len(numbers) == 2:
        return (numbers[0] * numbers[1]) / gcd(numbers[0], numbers[1])

    while len(numbers) > 2:
        numbers[1] = lcm([numbers[1], numbers[2]])
        numbers.pop(2)
    
    return lcm([numbers[0], numbers[1]])


def part1(nodes_raw, instructions):
    nodes = {}
    for node in nodes_raw:
        nodes[node.split(" = ")[0]] = node.split(" = ")[1][1:-1].split(", ")

    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current_node = nodes[current_node][0]
            elif instruction == "R":
                current_node = nodes[current_node][1]
            steps += 1

    return steps


def part2(nodes_raw, instructions):
    nodes = {}
    a_nodes = []
    z_nodes = []
    for node in nodes_raw:
        if node.split(" = ")[0][2] == "A":
            a_nodes.append(node.split(" = ")[0])
        elif node.split(" = ")[0][2] == "A":
            z_nodes.append(node.split(" = ")[0])
        nodes[node.split(" = ")[0]] = node.split(" = ")[1][1:-1].split(", ")

    nodes_mapped = {}
    for node in nodes:
        current_node = node
        for instruction in instructions:
            if instruction == "L":
                current_node = nodes[current_node][0]
            elif instruction == "R":
                current_node = nodes[current_node][1]
        nodes_mapped[node] = current_node

    steps = 0
    a_to_z = {}
    for a_node in a_nodes:
        a_to_z[a_node] = 0 
        visited = set()
        current_node = a_node
        while current_node not in visited:
            if current_node[2] == "Z":
                a_to_z[a_node] = steps
            visited.add(current_node)
            current_node = nodes_mapped[current_node]
            steps += 1
        steps = 0

    return int(lcm(list([val for val in a_to_z.values()])) * len(instructions))


with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    instructions = lines[0]
    nodes_raw = lines[2:]

    print("part1:", part1(nodes_raw, instructions))
    print("part2:", part2(nodes_raw, lines[0]))


