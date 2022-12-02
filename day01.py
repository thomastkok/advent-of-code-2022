def part_one(calories):
    max([sum(map(lambda x: int(x), y.split("\n"))) for y in calories.split("\n\n")])


def part_two(calories):
    sum(sorted([sum(map(lambda x: int(x), y.split("\n"))) for y in calories.split("\n\n")])[-3:])
