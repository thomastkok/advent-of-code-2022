def get_cycles(commands):
    cycles = [1]
    for command in commands.splitlines():
        if command == "noop":
            cycles.append(cycles[-1])
        else:
            cycles.append(cycles[-1])
            cycles.append(cycles[-1] + int(command.split(" ")[1]))
    return cycles


def part_one(commands):
    cycles = get_cycles(commands)
    return sum([x * cycles[x - 1] for x in range(20, len(cycles), 40)])


def part_two(commands):
    cycles = get_cycles(commands)
    drawing = []
    for i, pixel in enumerate(cycles):
        drawing.append("#" if abs(pixel - i % 40) < 2 else ".")
    for i in range(6):
        print("".join(drawing[i * 40 : i * 40 + 40]))
