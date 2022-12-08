from itertools import product
from math import prod

import numpy as np


def part_one(trees):
    def _is_visible(arr, x, y):
        for dir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            k = 1
            while x + k * dir[0] >= 0 and x + k * dir[0] < arr.shape[0] and y + k * dir[1] >= 0 and y + k * dir[1] < arr.shape[1]:
                if arr[x + k * dir[0], y + k * dir[1]] >= arr[x, y]:
                    break
                k += 1
            else:
                return True
        return False

    arr = np.array([x for x in list(trees) if x.isdigit()], dtype=int).reshape((99, 99))
    return sum([int(_is_visible(arr, i, j)) for i, j in product(range(arr.shape[0]), range(arr.shape[1]))])


def part_two(trees):
    def _scenic_score(arr, x, y):
        dir_scores = []
        for dir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            k = 1
            while x + k * dir[0] >= 0 and x + k * dir[0] < arr.shape[0] and y + k * dir[1] >= 0 and y + k * dir[1] < arr.shape[1]:
                if arr[x + k * dir[0], y + k * dir[1]] >= arr[x, y]:
                    k += 1
                    break
                k += 1
            dir_scores.append(k - 1)
        return prod(dir_scores)

    arr = np.array([x for x in list(trees) if x.isdigit()], dtype=int).reshape((99, 99))
    return max([_scenic_score(arr, i, j) for i, j in product(range(arr.shape[0]), range(arr.shape[1]))])
