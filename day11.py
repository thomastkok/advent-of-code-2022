from math import prod


def part_one(puzzle_input, n_loops=20):
    monkey_items, inspection_counts = {}, {}
    for monkey in puzzle_input.split("Monkey")[1:]:
        id = int(monkey[1])
        for j, line in enumerate(monkey.splitlines()):
            if "Starting items" in line:
                monkey_items[id] = [int(x) for x in line.split(": ")[1].split(", ")]
        inspection_counts[id] = 0
    for i in range(n_loops):
        for monkey in puzzle_input.split("Monkey")[1:]:
            id = int(monkey[1])
            for j, line in enumerate(monkey.splitlines()):
                if "Operation" in line:
                    inspection_counts[id] += len(monkey_items[id])
                    expr = line.split("new = ")[1]
                    for k, old in enumerate(monkey_items[id]):
                        monkey_items[id][k] = eval(expr) // 3
                if "Test" in line:
                    div = int(line.split("divisible by ")[1])
                    for k, item in enumerate(monkey_items[id]):
                        monkey_items[int(monkey.splitlines()[j + (1 if item % div == 0 else 2)].split("throw to monkey ")[1])].append(item)
                    monkey_items[id] = []
    return sorted(inspection_counts.values())[-1] * sorted(inspection_counts.values())[-2]


def part_two(puzzle_input, n_loops=10000):
    monkey_items, inspection_counts = {}, {}
    mod_factor = prod([int(line.split("divisible by ")[1]) for line in puzzle_input.splitlines() if "Test" in line])
    for monkey in puzzle_input.split("Monkey")[1:]:
        id = int(monkey[1])
        for j, line in enumerate(monkey.splitlines()):
            if "Starting items" in line:
                monkey_items[id] = [int(x) for x in line.split(": ")[1].split(", ")]
        inspection_counts[id] = 0
    for i in range(n_loops):
        for monkey in puzzle_input.split("Monkey")[1:]:
            id = int(monkey[1])
            for j, line in enumerate(monkey.splitlines()):
                if "Operation" in line:
                    inspection_counts[id] += len(monkey_items[id])
                    expr = line.split("new = ")[1]
                    for k, old in enumerate(monkey_items[id]):
                        monkey_items[id][k] = eval(expr) % mod_factor
                if "Test" in line:
                    div = int(line.split("divisible by ")[1])
                    for k, item in enumerate(monkey_items[id]):
                        monkey_items[int(monkey.splitlines()[j + (1 if item % div == 0 else 2)].split("throw to monkey ")[1])].append(item)
                    monkey_items[id] = []
    return sorted(inspection_counts.values())[-1] * sorted(inspection_counts.values())[-2]
