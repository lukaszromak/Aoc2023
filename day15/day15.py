def hash_function(string):
    current_val = 0

    for char in string:
        current_val += ord(char)
        current_val *= 17
        current_val = current_val % 256

    return current_val

with open("input.txt") as file:
    sequence = file.readline().strip().split(",")
    print(sum([hash_function(x) for x in sequence]))