def get_sensors(puzzle):
    read_coordinates = lambda x: (int(x.split("=")[1].split(",")[0]), int(x.split("=")[-1]))

    sensors = []
    beacons = []
    for line in puzzle.splitlines():
        sensor = read_coordinates(line.split("Sensor at ")[1].split(": ")[0])
        beacon = read_coordinates(line.split("beacon is at ")[1])
        sensors.append(sensor)
        beacons.append(beacon)


def get_distances(sensors, beacons):
    distances = []
    for sensor, beacon in zip(sensors, beacons):
        distances.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) + 1)
    return distances


def part_one(puzzle, y=10):
    sensors, beacons = get_sensors(puzzle)
    occupied = set()
    for sensor, beacon in zip(sensors, beacons):
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if distance < abs(sensor[1] - y):
            continue
        occupied.update(range(sensor[0] - (distance - abs(sensor[1] - y)), sensor[0] + (distance - abs(sensor[1] - y))))
    return len(sorted(occupied))


def part_two(puzzle, size=4000000):
    sensors, beacons = get_sensors(puzzle)
    distances = get_distances(sensors, beacons)
    for sensor, distance in zip(sensors, distances):
        left = -distance if sensor[0] - distance >= 0 else -sensor[0]
        right = distance if sensor[0] + distance <= size else size - sensor[0]
        for x in range(left, right + 1, 1):
            point = (sensor[0] + x, sensor[1] + distance - abs(x))
            if point[0] >= 0 and point[0] <= size and point[1] >= 0 and point[1] <= size:
                for s, d in zip(sensors, distances):
                    if abs(point[0] - s[0]) + abs(point[1] - s[1]) < d:
                        break
                else:
                    return point[0] * size + point[1]
            if distance != abs(x):
                point = (sensor[0] + x, sensor[1] - distance + abs(x))
                if point[0] >= 0 and point[0] <= size and point[1] >= 0 and point[1] <= size:
                    for s, d in zip(sensors, distances):
                        if abs(point[0] - s[0]) + abs(point[1] - s[1]) < d:
                            break
                    else:
                        return point[0] * size + point[1]
