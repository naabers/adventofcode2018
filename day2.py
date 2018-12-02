def part_a():
    exactly_two = 0
    exactly_three = 0
    lines = open('inputs/day2.txt').readlines()

    for line in lines:
        letter_count = {}
        for letter in line:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        found_two = False
        found_three = False
        for k, v in letter_count.items():
            if v == 2 and not found_two:
                found_two = True
                exactly_two += 1
            elif v == 3 and not found_three:
                found_three = True
                exactly_three += 1

    return exactly_two * exactly_three


def part_b():
    lines = open('inputs/day2.txt').readlines()
    for outer in lines:
        for inner in lines:

            found_difference = ''
            for i in range(len(inner)):
                if outer[i] != inner[i]:
                    if found_difference is not '':
                        found_difference = ''
                        break
                    found_difference = inner[i]

            if found_difference is not '':
                return (inner, found_difference)


def main():
    print(part_a())
    print(part_b())


if __name__ == '__main__':
    main()
