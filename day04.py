def part_one(assignments):
    return sum(
        [
            (lambda y: 1 if set(y[0]).issubset(set(y[1])) or set(y[1]).issubset(set(y[0])) else 0)(
                list(map(lambda x: range(int(x.split("-")[0]), int(x.split("-")[1]) + 1), line.split(",")))
            )
            for line in assignments.splitlines()
        ]
    )


def part_two(assignments):
    return sum(
        [
            (lambda y: 1 if len(set(y[0]) & set(y[1])) > 0 else 0)(list(map(lambda x: range(int(x.split("-")[0]), int(x.split("-")[1]) + 1), line.split(","))))
            for line in assignments.splitlines()
        ]
    )
