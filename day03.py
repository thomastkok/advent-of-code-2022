from functools import reduce


def part_one(rucksacks):
    return sum(map(lambda x: ord(x) - 38 if x.isupper() else ord(x) - 96, [(set(y[: len(y) // 2]) & set(y[len(y) // 2 :])).pop() for y in rucksacks.split("\n")]))


def part_two(rucksacks):
    return sum(
        map(
            lambda x: ord(x) - 38 if x.isupper() else ord(x) - 96,
            [reduce(lambda a, b: a & b, map(set, [rucksacks.split("\n")[i + j] for j in range(3)])).pop() for i in range(0, len(rucksacks.split("\n")) - 2, 3)],
        )
    )
