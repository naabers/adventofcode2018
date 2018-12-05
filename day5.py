import string


def react(letters):
    found_reaction = True
    while found_reaction:
        found_reaction = False
        for index in range(len(letters)):
            if index == len(letters) - 1:
                break

            if letters[index].islower():
                if letters[index].upper() == letters[index + 1]:
                    letters = letters[:index] + letters[index+2:]
                    found_reaction = True
                    break
            else:
                if letters[index].lower() == letters[index + 1]:
                    letters = letters[:index] + letters[index+2:]
                    found_reaction = True
                    break
    return len(letters)


def part_a():
    letters = open('inputs/day5.txt').read()
    return react(letters)


def part_b():
    letters = open('inputs/day5.txt').read()
    scores = {}
    for letter in string.ascii_lowercase:
        temp = letters
        temp = temp.replace(letter, '')
        temp = temp.replace(letter.upper(), '')
        scores[letter] = react(temp)

    best_value = scores['a']
    for letter, value in scores.items():
        if value < best_value:
            best_value = value
    return best_value


def main():
    print(part_a())
    print(part_b())


if __name__ == '__main__':
    main()
