import random
import copy

def parse_input(lines):
    vertices = set()
    edges = []

    for line in lines:
        node, adjacent = line.split(": ")
        adjacent = adjacent.split(" ")

        vertices.add(node)

        for neighbour in adjacent:
            edges.append([node, neighbour])
            if neighbour not in vertices:
                vertices.add(neighbour)

    return len(vertices), edges


def contract(_edges, _num_vertices):
    edges = copy.deepcopy(_edges)
    num_vertices = copy.deepcopy(_num_vertices)

    while num_vertices > 2:
        edge = random.choice(edges)
        node1, node2 = edge
        merged_node = "{},{}".format(node1, node2)

        idx = edges.index(edge)
        edges.pop(idx)

        for idx in range(len(edges) - 1, -1, -1):
            if (edges[idx][0] == node1 and edges[idx][1] == node2) or (edges[idx][0] == node2 and edges[idx][1] == node1):
                edges.pop(idx)
                continue
            if edges[idx][0] == node1:
                edges[idx][0] = merged_node
            if edges[idx][0] == node2:
                edges[idx][0] = merged_node
            if edges[idx][1] == node1:
                edges[idx][1] = merged_node
            if edges[idx][1] == node2:
                edges[idx][1] = merged_node

        num_vertices += -1

    return edges, len([idx for idx, _ in enumerate(edges) if _ is not None])


def karger(_edges, num_vertices, cut):
    edges = None
    cut_found = 0

    while cut_found != cut:
        edges, cut_found = contract(_edges, num_vertices)

    node1, node2 = next(edge for edge in edges if edge is not None)
    
    return len(node1.split(",")) * len(node2.split(","))


with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]
    num_vertices, edges = parse_input(lines)
    print(karger(edges, num_vertices, 3))