from itertools import product

import numpy as np


def get_padded_grid(puzzle):
    grid = np.zeros((len(puzzle.splitlines()), len(puzzle.splitlines()[0])), dtype=int)

    for i, line in enumerate(puzzle.splitlines()):
        for j, char in enumerate(line):
            if char == "#":
                grid[i, j] = 1

    grid = np.pad(grid, (100, 100))


def find_direction(direction, elf, grid):
    if direction == "N" and sum([grid[x] for x in [(elf[0] + a, elf[1] + b) for a, b in product([-1], [-1, 0, 1])]]) == 0:
        return (-1, 0)
    elif direction == "S" and sum([grid[x] for x in [(elf[0] + a, elf[1] + b) for a, b in product([1], [-1, 0, 1])]]) == 0:
        return (1, 0)
    elif direction == "W" and sum([grid[x] for x in [(elf[0] + a, elf[1] + b) for a, b in product([-1, 0, 1], [-1])]]) == 0:
        return (0, -1)
    elif direction == "E" and sum([grid[x] for x in [(elf[0] + a, elf[1] + b) for a, b in product([-1, 0, 1], [1])]]) == 0:
        return (0, 1)
    else:
        return None


def simulate_round(grid, round):
    i, j = np.where(grid == 1)
    elves = list(zip(list(i), list(j)))
    targets = {}
    for elf in elves:
        neighbors = [(elf[0] + a, elf[1] + b) for a, b in product([-1, 0, 1], [-1, 0, 1])]
        if sum([grid[x] for x in neighbors]) == 1:
            continue

        direction = None
        order = "NSWE"[round % 4 :] + "NSWE"[: round % 4]
        for d in order:
            if find_direction(d, elf, grid) is not None:
                direction = find_direction(d, elf, grid)
                break
        if direction is None:
            continue
        targets[elf] = (elf[0] + direction[0], elf[1] + direction[1])

    unique_targets = [tuple(a) for a, b in zip(*np.unique(list(targets.values()), return_counts=True, axis=0)) if b == 1]

    if len(unique_targets) == 0:
        return None

    for elf, target in targets.items():
        if target in unique_targets:
            grid[elf] = 0
            grid[target] = 1

    return grid


def part_one(puzzle, rounds=10):
    grid = get_padded_grid(puzzle)

    for i in range(rounds):
        grid = simulate_round(grid, i)

    x_min, x_max = np.where(grid == 1)[0].min(), np.where(grid == 1)[0].max()
    y_min, y_max = np.where(grid == 1)[1].min(), np.where(grid == 1)[1].max()

    return np.count_nonzero(grid[x_min : x_max + 1, y_min : y_max + 1] == 0)


def part_two(puzzle):
    grid = get_padded_grid(puzzle)

    for i in range(10000):
        grid = simulate_round(grid, i)
        if grid is None:
            return i + 1
