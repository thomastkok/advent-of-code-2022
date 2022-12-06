def part_one(input_string):
    for i in range(len(input_string)):
        if len(set(input_string[i : i + 4])) == 4:
            return i + 4


def part_two(input_string):
    for i in range(len(input_string)):
        if len(set(input_string[i : i + 14])) == 14:
            return i + 14
