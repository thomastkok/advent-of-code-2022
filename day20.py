def part_one(puzzle):
    encrypted = [int(x) for x in puzzle.splitlines()]
    decrypted, indices = list(encrypted), list(range(len(encrypted)))

    for i, val in enumerate(encrypted):
        j = indices.index(i)
        v_, i_ = decrypted.pop(j), indices.pop(j)
        decrypted.insert((j + val) % (len(decrypted)), v_)
        indices.insert((j + val) % (len(indices)), i_)

    zero_index = decrypted.index(0)
    return sum([decrypted[(zero_index + x) % len(decrypted)] for x in [1000, 2000, 3000]])


def part_two(puzzle):
    encrypted = [int(x) * 811589153 for x in puzzle.splitlines()]
    decrypted, indices = list(encrypted), list(range(len(encrypted)))

    for _ in range(10):
        for i, val in enumerate(encrypted):
            j = indices.index(i)
            v_, i_ = decrypted.pop(j), indices.pop(j)
            decrypted.insert((j + val) % (len(decrypted)), v_)
            indices.insert((j + val) % (len(indices)), i_)

    zero_index = decrypted.index(0)
    return sum([decrypted[(zero_index + x) % len(decrypted)] for x in [1000, 2000, 3000]])
