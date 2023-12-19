import operator
import copy
import os
from functools import reduce

def parse_input(input_):
    input_ = input_.split("\n\n")
    input_[0] = input_[0].split("\n")
    input_[1] = input_[1].split("\n")

    workflows = {}
    for line in input_[0]:
        workflow_name, rules = line.strip().split("{")
        rules = rules[:-1].split(",")
        workflows[workflow_name] = rules

    parts = []
    for line in input_[1]:
        rating = {}
        for r in line[1:-1].split(","):
            r_name, r_value = r.split("=")
            rating[r_name] = int(r_value)
        parts.append(rating)

    return workflows, parts


def process_parts(workflows, parts):
    OPS = {
        "<" : operator.lt,
        ">" : operator.gt
    }
    count = 0

    for part in parts:
        workflow = "in"

        while workflow != "A" and workflow != "R":
            rules = workflows[workflow]

            for idx, rule in enumerate(rules):
                if idx == len(rules) - 1:
                    workflow = rule
                    continue

                condition, destination = rule.split(":")
                rating, op, operand = condition[0], condition[1], int(condition[2:])

                if OPS[op](part[rating], operand):
                    workflow = destination
                    break

        if workflow == "A":
            count += sum([x for x in part.values()])

    return count


def range_intersection(range_a, range_b):
    if range_b[0] > range_a[1] or range_a[0] > range_b[1]:
        return 0
    return (max(range_a[0], range_b[0]), min(range_a[1], range_b[1]))


def find_combinations(workflow, _conditions, workflows):
    conditions = copy.deepcopy(_conditions)
    if workflow == "A":
        multiplier = pow(4000, (4 - len(conditions)))
        return reduce(lambda x, y: x * y, [x[1] - x[0] + 1 for x in conditions.values()]) * multiplier
    if workflow == "R":
        return 0
    
    count = 0

    for idx, rule in enumerate(workflows[workflow]):
        if idx == len(workflows[workflow]) - 1:
            count += find_combinations(rule, conditions, workflows)
            continue

        condition, destination = rule.split(":")
        rating, op, operand = condition[0], condition[1], int(condition[2:])

        if rating not in conditions:
            if op == "<":
                count += find_combinations(destination, conditions | {rating: (1, operand - 1)}, workflows)
                conditions[rating] = (operand, 4000)
            elif op == ">":
                count += find_combinations(destination, conditions | {rating: (operand + 1, 4000)}, workflows)
                conditions[rating] = (1, operand)     
        elif rating in conditions:
            prev_range = copy.deepcopy(conditions[rating])
            if op == "<":
                entry_range = range_intersection((1, operand - 1), prev_range)
                continue_range = range_intersection((operand, 4000), prev_range)
            elif op == ">":
                entry_range = range_intersection((operand + 1, 4000), prev_range)
                continue_range = range_intersection((1, operand), prev_range)

            conditions[rating] = entry_range
            count += find_combinations(destination, conditions, workflows)
            conditions[rating] = continue_range

    return count


with open(os.path.dirname(os.path.realpath(__file__)) + "\\input.txt") as file:
    input_ = file.read()
    workflows, parts = parse_input(input_)

    print("part1:", process_parts(workflows, parts))
    print("part2:", find_combinations("in", dict(), workflows))