def process_line(line, total):
    if line[0] == '+':
        total += int(line[1:])
    else:
        total -= int(line[1:])
    return total


def part_a():
    total = 0
    lines = open('inputs/day1.txt').readlines()
    for line in lines:
        total = process_line(line, total)
    return total


def part_b():
    total = 0
    seen = set()
    lines = open('inputs/day1.txt').readlines()
    while True:
        for line in lines:
            total = process_line(line, total)

            if total not in seen:
                seen.add(total)
            else:
                return total


def main():
    print(part_a())
    print(part_b())


if __name__ == '__main__':
    main()
