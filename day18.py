import numpy as np


def get_shape(cubes):
    shape = np.zeros((21, 21, 21), dtype=int)
    for cube in cubes.splitlines():
        loc = tuple([int(x) for x in cube.split(",")])
        shape[loc] = 1
    return shape


def part_one(cubes):
    shape = get_shape(cubes)
    total = 0
    for (x, y, z), val in np.ndenumerate(shape):
        if val == 1:
            total += 6 - (sum([shape[x + a, y + b, z + c] for a, b, c in zip([-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1])]))
    return total


def part_two(cubes):
    shape = get_shape(cubes)
    for (x, y, z), val in np.ndenumerate(shape):
        if val == 0:
            count = 0
            for a, b, c in zip([-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]):
                i = 1
                while x + i * a >= 0 and x + i * a < 21 and y + i * b >= 0 and y + i * b < 21 and z + i * c >= 0 and z + i * c < 21:
                    if shape[x + i * a, y + i * b, z + i * c] == 1:
                        count += 1
                        break
                    i += 1
                else:
                    break
            if count == 6:
                shape[x, y, z] = -1

    total = 0
    for (x, y, z), val in np.ndenumerate(shape):
        if val == 1:
            for a, b, c in zip([-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]):
                if shape[x + a, y + b, z + c] == 0:
                    total += 1
    return total
