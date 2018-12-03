FILENAME = 'inputs/day3.txt'


def get_coordinates(line):
    after_at = line.split('@')[1].strip()
    start_x = int(after_at.split(',')[0])
    start_y = int(after_at.split(',')[1].split(':')[0])
    distance_x = int(after_at.split(':')[1].strip().split('x')[0])
    distance_y = int(after_at.split(':')[1].strip().split('x')[1])
    return start_x, start_y, distance_x, distance_y


def get_fabric_layout():
    fabric = {}
    lines = open(FILENAME).readlines()
    for line in lines:
        start_x, start_y, distance_x, distance_y = get_coordinates(line)

        for mod_x in range(distance_x):
            for mod_y in range(distance_y):
                x = start_x + mod_x + 1
                y = start_y + mod_y + 1
                fabric['{}x{}'.format(x, y)] = fabric.get('{}x{}'.format(x, y), 0) + 1
    return fabric


def part_a():
    fabric = get_fabric_layout()

    overlap = 0
    for key, value in fabric.items():
        if value > 1:
            overlap += 1

    return overlap


def part_b():
    fabric = get_fabric_layout()

    lines = open(FILENAME).readlines()
    for line in lines:
        start_x, start_y, distance_x, distance_y = get_coordinates(line)

        overlap = False
        for mod_x in range(distance_x):
            for mod_y in range(distance_y):
                x = start_x + mod_x + 1
                y = start_y + mod_y + 1
                if fabric['{}x{}'.format(x, y)] != 1:
                    overlap = True
                    break
            if overlap:
                break
        if not overlap:
            return line


def main():
    print(part_a())
    print(part_b())


if __name__ == '__main__':
    main()
