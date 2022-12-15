import numpy as np


def get_rocks(puzzle):
    rocks = []
    for line in puzzle.splitlines():
        path = [eval(x) for x in line.split(" -> ")]
        rock_path = []
        for i in range(len(path) - 1):
            line = []
            if path[i][0] != path[i + 1][0]:
                step = 1 if path[i + 1][0] > path[i][0] else -1
                line = [(x, path[i][1]) for x in range(path[i][0], path[i + 1][0], step)]
            else:
                step = 1 if path[i + 1][1] > path[i][1] else -1
                line = [(path[i][0], x) for x in range(path[i][1], path[i + 1][1], step)]
            rock_path.extend(line)
        rock_path.append(path[-1])
        rocks.extend(rock_path)
    return rocks


def sim_sand(cave, spawn_point):
    position = spawn_point
    if cave[spawn_point] == 1:
        return cave, True
    while True:
        if position[0] + 1 >= cave.shape[0]:
            return cave, True
        elif cave[(position[0] + 1, position[1])] == 0:
            position = (position[0] + 1, position[1])
        elif position[1] - 1 < 0:
            return cave, True
        elif cave[(position[0] + 1, position[1] - 1)] == 0:
            position = position[0] + 1, position[1] - 1
        elif position[1] + 1 >= cave.shape[1]:
            return cave, True
        elif cave[(position[0] + 1, position[1] + 1)] == 0:
            position = position[0] + 1, position[1] + 1
        else:
            cave[position] = 1
            return cave, False


def part_one(puzzle):
    rocks = get_rocks(puzzle)
    x_min, x_max = min(rocks, key=lambda x: x[0])[0], max(rocks, key=lambda x: x[0])[0]
    y_min, y_max = 0, max(rocks, key=lambda x: x[1])[1]
    cave = np.zeros((y_max + 1, x_max - x_min + 1), dtype=int)
    sand_spawn = (0, 500 - x_min)
    for rock in rocks:
        cave[(rock[1], rock[0] - x_min)] = 1
    counter = 0
    while True:
        cave, to_break = sim_sand(cave, sand_spawn)
        if to_break:
            break
        counter += 1
    return counter


def part_two(puzzle):
    rocks = get_rocks(puzzle)
    x_min, x_max = min(rocks, key=lambda x: x[0])[0], max(rocks, key=lambda x: x[0])[0]
    y_min, y_max = 0, max(rocks, key=lambda x: x[1])[1]
    cave = np.zeros((y_max + 1 + 2, x_max - x_min + 1 + 10000), dtype=int)
    sand_spawn = (0, 500 - x_min + 5000)
    for rock in rocks:
        cave[(rock[1], rock[0] - x_min + 5000)] = 1
    cave[y_max + 2, :] = 1
    counter = 0
    while True:
        cave, to_break = sim_sand(cave, sand_spawn)
        if to_break:
            break
        counter += 1
    return counter
