def get_initial_dicts(monkeys):
    waiting_monkeys = {}
    yelling_monkeys = {}

    for monkey in monkeys.splitlines():
        name, job = monkey.split(": ")
        if job.isdigit():
            yelling_monkeys[name] = int(job)
        else:
            symbol = job.split(" ")[1].split(" ")[0]
            waiting_monkeys[name] = job.split(f" {symbol} "), symbol

    return waiting_monkeys, yelling_monkeys


def part_one(monkeys):
    waiting_monkeys, yelling_monkeys = get_initial_dicts(monkeys)
    while "root" in waiting_monkeys:
        for name in list(waiting_monkeys.keys()):
            job = waiting_monkeys[name]
            if job[0][0] in yelling_monkeys and job[0][1] in yelling_monkeys:
                yelling_monkeys[name] = int(eval(f"yelling_monkeys[job[0][0]] {job[1]} yelling_monkeys[job[0][1]]"))
                del waiting_monkeys[name]
    else:
        return yelling_monkeys["root"]


def part_two(monkeys):
    waiting_monkeys, yelling_monkeys = get_initial_dicts(monkeys)
    last_len = -1
    yelling_monkeys.pop("humn")
    while "root" in waiting_monkeys:
        new_len = list(waiting_monkeys.keys())
        if new_len == last_len:
            break
        last_len = new_len
        for name in list(waiting_monkeys.keys()):
            if name == "root" or name == "humn":
                continue
            job = waiting_monkeys[name]
            if job[0][0] in yelling_monkeys and job[0][1] in yelling_monkeys:
                yelling_monkeys[name] = int(eval(f"yelling_monkeys[job[0][0]] {job[1]} yelling_monkeys[job[0][1]]"))
                del waiting_monkeys[name]

    for name, job in waiting_monkeys.items():
        if job[0][0] in yelling_monkeys:
            job[0][0] = yelling_monkeys[job[0][0]]
        if job[0][1] in yelling_monkeys:
            job[0][1] = yelling_monkeys[job[0][1]]

    node = "root"
    while node != "humn":
        if node == "root":
            var_index = 1 if isinstance(waiting_monkeys[node][0][0], int) else 0
            var = waiting_monkeys[node][0][var_index]
            yelling_monkeys[var] = waiting_monkeys[node][0][1 - var_index]
            prev_node = node
            node = var
        else:
            var_index = 1 if isinstance(waiting_monkeys[node][0][0], int) else 0
            var = waiting_monkeys[node][0][var_index]
            symbol = waiting_monkeys[node][1]
            if symbol == "/" and var_index == 0:
                yelling_monkeys[var] = yelling_monkeys[node] * waiting_monkeys[node][0][1]
            elif symbol == "/" and var_index == 1:
                yelling_monkeys[var] = waiting_monkeys[node][0][1] // yelling_monkeys[node]
            elif symbol == "*":
                yelling_monkeys[var] = yelling_monkeys[node] // waiting_monkeys[node][0][1 - var_index]
            elif symbol == "-" and var_index == 0:
                yelling_monkeys[var] = yelling_monkeys[node] + waiting_monkeys[node][0][1 - var_index]
            elif symbol == "-" and var_index == 1:
                yelling_monkeys[var] = waiting_monkeys[node][0][1 - var_index] - yelling_monkeys[node]
            elif symbol == "+":
                yelling_monkeys[var] = yelling_monkeys[node] - waiting_monkeys[node][0][1 - var_index]
            prev_node = node
            node = var
        del waiting_monkeys[prev_node]
    else:
        return yelling_monkeys["humn"]
