import numpy as np


def read_map(heightmap):
    grid = np.array([ord(x) - 96 for x in heightmap if x != "\n"]).reshape((41, 144))
    start = np.where(grid == -13)
    start = start[0][0], start[1][0]
    end = np.where(grid == -27)
    end = end[0][0], end[1][0]
    return grid, start, end


def get_elevation(position, grid):
    if grid[position] > 0:
        return grid[position]
    elif grid[position] == -13:
        return 1
    elif grid[position] == -27:
        return 26


def get_neighbors(position, visited_positions, grid, part):
    neighbors = []
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if position[0] + dir[0] >= 0 and position[0] + dir[0] < grid.shape[0] and position[1] + dir[1] >= 0 and position[1] + dir[1] < grid.shape[1]:
            if part == "one":
                if get_elevation((position[0] + dir[0], position[1] + dir[1]), grid) <= get_elevation(position, grid) + 1:
                    if (position[0] + dir[0], position[1] + dir[1]) not in visited_positions:
                        neighbors.append((position[0] + dir[0], position[1] + dir[1]))
            elif part == "two":
                if get_elevation((position[0] + dir[0], position[1] + dir[1]), grid) >= get_elevation(position, grid) - 1:
                    if (position[0] + dir[0], position[1] + dir[1]) not in visited_positions:
                        neighbors.append((position[0] + dir[0], position[1] + dir[1]))
    return neighbors


def part_one(heightmap):
    grid, start, end = read_map(heightmap)
    visited_positions = {start: 0}
    working_queue = [start]
    while len(working_queue) > 0:
        element = working_queue.pop(0)
        if grid[element] == -27:
            return visited_positions[element]
        else:
            neighbors = get_neighbors(element, visited_positions.keys(), grid, part="one")
            working_queue.extend(neighbors)
            for neighbor in neighbors:
                visited_positions[neighbor] = visited_positions[element] + 1


def part_two(heightmap):
    grid, start, end = read_map(heightmap)
    visited_positions = {end: 0}
    working_queue = [end]
    while len(working_queue) > 0:
        element = working_queue.pop(0)
        if get_elevation(element, grid) == 1:
            return visited_positions[element]
        else:
            neighbors = get_neighbors(element, visited_positions.keys(), grid, part="two")
            working_queue.extend(neighbors)
            for neighbor in neighbors:
                visited_positions[neighbor] = visited_positions[element] + 1
