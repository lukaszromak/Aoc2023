from queue import Queue
from functools import reduce
import copy
import networkx as nx 
import matplotlib.pyplot as plt 

def parse_input(lines):
    modules = {}

    for line in lines:
        module, destinations = line.split(" -> ")
        if module == "broadcaster":
            modules[module] = {"type": "broadcaster", "outputs": destinations.split(", ")}
        elif module[0] == "%":
            modules[module[1:]] = {"type": "flipflop", "outputs": destinations.split(", "), "state": False}
        elif module[0] == "&":
            modules[module[1:]] = {"type": "conjunction", "outputs": destinations.split(", "), "state": {}}

    #find conjunction modules inputs
    for key, module in modules.items():
        if module["type"] == "conjunction":
            for key2, module2 in modules.items():
                if key in module2["outputs"]:
                    modules[key]["state"][key2] = False

    return modules


def visualize_modules(modules):
    edges = []
    for module in modules:
        for destination in modules[module]["outputs"]:
            edges.append([module, destination])

    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    nx.draw_networkx(graph, pos=nx.spring_layout(graph))
    plt.savefig("graph.png")


def push_button(_modules, states_to_find):
    modules = copy.deepcopy(_modules)
    queue = Queue()
    queue.put(("broadcaster", False, "broadcaster"))
    pulses_released = [0, 0]
    states_found = []

    while not queue.empty():
        module, pulse, sender = queue.get()

        if sender in states_to_find and pulse and module == "ft":
            states_found.append(sender)

        if pulse:
            pulses_released[0] += 1
        else:
            pulses_released[1] += 1

        if module not in modules.keys():
            continue

        module_type = modules[module]["type"]

        if module_type == "broadcaster":
            for output in modules[module]["outputs"]:
                queue.put((output, False, module))

        if module_type == "flipflop":
            if pulse == 1:
                continue

            modules[module]["state"] = not modules[module]["state"]

            for output in modules[module]["outputs"]:
                queue.put((output, modules[module]["state"], module))

        if module_type == "conjunction":
            modules[module]["state"][sender] = pulse
            output_pulse = not all(modules[module]["state"].values())

            for output in modules[module]["outputs"]:
                queue.put((output, output_pulse, module))


    if len(states_to_find) > 0:
        return states_found, modules
    return pulses_released, modules


def push_button_num_times(modules, times):
    positive_pulses = 0
    negative_pulses = 0

    for _ in range(times):
        pulses_released,  modules = push_button(modules, [])
        positive_pulses += pulses_released[0]
        negative_pulses += pulses_released[1]

    return positive_pulses * negative_pulses


def find_pulses_to_rx(modules):
    states_to_find = ["qh", "lt", "vz", "bq"]
    cycles_found = []

    cycle = 1
    while len(cycles_found) < 4:
        states, modules = push_button(modules, states_to_find)
        for state in states:
            states_to_find.remove(state)
            cycles_found.append(cycle)
        cycle += 1
    
    return reduce(lambda x, y: x * y, [x for x in cycles_found])


with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    modules = parse_input(lines)
    print("part1:", push_button_num_times(modules, 1000))
    print("part2:", find_pulses_to_rx(modules))