from functools import cmp_to_key


def compare(left, right, part="one"):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1 if part == "one" else -1
        elif left > right:
            return 0 if part == "one" else 1
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        if not left and right:
            return 1 if part == "one" else -1
        elif not right and left:
            return 0 if part == "one" else 1
        elif not right and not left:
            return None
        else:
            if compare(left[0], right[0]) is not None:
                return compare(left[0], right[0])
            else:
                return compare(left[1:], right[1:])
    else:
        if isinstance(left, int):
            return compare([left], right)
        elif isinstance(right, int):
            return compare(left, [right])


def part_one(puzzle):
    return sum([(i + 1) * compare(*[eval(x) for x in pair.split("\n")]) for i, pair in enumerate(puzzle.split("\n\n"))])


def part_two(puzzle):
    puzzle_list = [eval(x) for x in puzzle.split("\n") if len(x) > 0]
    puzzle_list.append([[2]])
    puzzle_list.append([[6]])
    sorted_puzzle = sorted(puzzle_list, key=cmp_to_key(compare))
    return (sorted_puzzle.index([[2]]) + 1) * (sorted_puzzle.index([[6]]) + 1)
