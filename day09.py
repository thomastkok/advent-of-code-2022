def update_tail(head, tail):
    if abs(head[0] - tail[0]) > 1 and head[1] == tail[1]:
        return [tail[0] + (1 if head[0] > tail[0] else -1), tail[1]]
    elif abs(head[1] - tail[1]) > 1 and head[0] == tail[0]:
        return [tail[0], tail[1] + (1 if head[1] > tail[1] else -1)]
    elif abs(head[0] - tail[0]) + abs(head[1] - tail[1]) > 2:
        return [tail[0] + (1 if head[0] > tail[0] else -1), tail[1] + (1 if head[1] > tail[1] else -1)]
    else:
        return tail


def part_one(moves):
    head = [0, 0]
    tail = [0, 0]
    visited_positions = set()
    directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
    for line in moves.splitlines():
        dir, repeat = line.split(" ")
        for _ in range(int(repeat)):
            head = [head[0] + directions[dir][0], head[1] + directions[dir][1]]
            tail = update_tail(head, tail)
            visited_positions.add(tuple(tail))
    return len(visited_positions)


def part_two(moves):
    head = [0, 0]
    tails = {k: [0, 0] for k in range(9)}
    visited_positions = set()
    directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
    for line in moves.splitlines():
        dir, repeat = line.split(" ")
        for _ in range(int(repeat)):
            head = [head[0] + directions[dir][0], head[1] + directions[dir][1]]
            for i in range(9):
                tails[i] = update_tail(head if i == 0 else tails[i - 1], tails[i])
            visited_positions.add(tuple(tails[8]))
    return len(visited_positions)
