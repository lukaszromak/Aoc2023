def ends_with(nodes, char):
    for node in nodes:
        if node[2] != char:
            return False
    return True


with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    instructions = lines[0]
    nodes = {}
    a_nodes = []
    z_nodes = []
    for i in range(2, len(lines)):
        if lines[i].split(" = ")[0][2] == "A":
            a_nodes.append(lines[i].split(" = ")[0])
        elif lines[i].split(" = ")[0][2] == "A":
            z_nodes.append(lines[i].split(" = ")[0])
        nodes[lines[i].split(" = ")[0]] = lines[i].split(" = ")[1][1:-1].split(", ")

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
        a_to_z[a_node] = [] 
        visited = set()
        current_node = a_node
        while current_node not in visited:
            if current_node[2] == "Z":
                a_to_z[a_node].append(steps)
            visited.add(current_node)
            current_node = nodes_mapped[current_node]
            steps += 1
        visited = set()
        steps = 0
    print("just get a lcm of these values online and multiply them by len(instructions) xD")
    print(a_to_z)


