def read_data(input):
    original_stacks, commands = input.split("\n\n")
    n_stacks = int(original_stacks[-2])
    stacks = [[] for _ in range(n_stacks)]
    for line in original_stacks.split("\n 1")[0].splitlines()[::-1]:
        for i in range(n_stacks):
            if line[1 + 4 * i] != " ":
                stacks[i].append(line[1 + 4 * i])
    return stacks, commands


def part_one(stacks, commands):
    for command in commands.splitlines():
        how_many, from_st, to_st = [int(command.split(" ")[i]) for i in [1, 3, 5]]
        for _ in range(how_many):
            stacks[to_st - 1].append(stacks[from_st - 1].pop())
    return "".join([x[-1] for x in stacks])


def part_two(stacks, commands):
    for command in commands.splitlines():
        how_many, from_st, to_st = [int(command.split(" ")[i]) for i in [1, 3, 5]]
        stacks[to_st - 1].extend(stacks[from_st - 1][-how_many:])
        stacks[from_st - 1] = stacks[from_st - 1][:-how_many]
    return "".join([x[-1] for x in stacks])
