def hash_function(string):
    current_val = 0

    for char in string:
        current_val += ord(char)
        current_val *= 17
        current_val = current_val % 256

    return current_val


def parse_operations(sequence):
    operations = []

    for operation in sequence:
        if operation.count("-") == 1:
            operations.append(("-", operation[:-1]))
        elif operation.count("=") == 1:
            label, value = operation.split("=")
            operations.append(("=", label, value))

    return operations


def execute_operations(operations):
    boxes = [[] for x in range(256)]

    for operation in operations:
        op_code = operation[0]
        label = operation[1]
        box = hash_function(label)
        indices = [idx for idx, x in enumerate(boxes[box]) if x.split(" ")[0] == label]

        if op_code == "-":
            if len(indices) == 1:
                boxes[box].pop(indices[0])
        elif op_code == "=":
            value = operation[2]
            if len(indices) == 0:
                boxes[box].append("{} {}".format(label, value))
            else:    
                boxes[box] =  boxes[box][:indices[0]] + ["{} {}".format(label, value)] + boxes[box][indices[0] + 1:]

    return boxes


def calculate_focusing_power(boxes):
    return sum([int(label.split(" ")[1]) * (slot + 1) * (box + 1) for box, x in enumerate(boxes) for slot, label in enumerate(x)])


with open("input.txt") as file:
    sequence = file.readline().strip().split(",")
    
print("part1:", sum([hash_function(x) for x in sequence]))
print("part2:", calculate_focusing_power(execute_operations(parse_operations(sequence))))