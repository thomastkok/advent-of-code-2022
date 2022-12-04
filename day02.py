def part_one(rps, p1=["B", "C", "A"], p2=["X", "Y", "Z"]):
    return sum([p2.index(x[1]) + 1 + 3 * ((p2.index(x[1]) - p1.index(x[0])) % 3) for x in map(lambda x: x.split(" "), rps.split("\n"))])


def part_two(rps, p1={"A": 0, "B": 1, "C": 2}, res={"X": 0, "Y": 1, "Z": 2}):
    return sum([3 * res[x[1]] + (p1[x[0]] + res[x[1]] - 1) % 3 + 1 for x in map(lambda x: x.split(" "), rps.split("\n"))])
