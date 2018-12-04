from datetime import datetime, timedelta


FILENAME = 'inputs/day4.txt'


def parse_guard(line):
    line = line.split()
    for word in line:
        if '#' in word:
            return int(word[1:])


def get_line_time(line):
    datestring = line.split(']')[0].split('[')[1]
    return datetime.strptime(datestring, '%Y-%m-%d %H:%M')


def calculate_guards():
    lines = open(FILENAME).readlines()
    lines.sort(key=get_line_time)

    guards = {}
    guard = 0
    for line in lines:
        if 'Guard' in line:
            guard = parse_guard(line)
            continue
        elif 'falls asleep' in line:
            sleep = get_line_time(line)
        elif 'wakes up' in line:
            wake = get_line_time(line)
            sleep_array = guards.get(guard, [])
            while sleep < wake:
                sleep_array.append(sleep.minute)
                sleep = sleep + timedelta(seconds=60)
            guards[guard] = sleep_array
    return guards


def part_a():
    guards = calculate_guards()
    best_guard = 0
    time_asleep = []
    for guard, sleep in guards.items():
        if len(sleep) > len(time_asleep):
            best_guard = guard
            time_asleep = sleep

    return best_guard * max(set(time_asleep), key=time_asleep.count)


def part_b():
    guards = calculate_guards()
    best_guard = 0
    most_frequent = 0
    highest_count = 0
    for guard, sleep in guards.items():
        temp_most_frequent = max(set(sleep), key=sleep.count)
        temp_highest_count = sleep.count(temp_most_frequent)
        if temp_highest_count > highest_count:
            best_guard = guard
            most_frequent = temp_most_frequent
            highest_count = temp_highest_count

    return best_guard * most_frequent


def main():
    print(part_a())
    print(part_b())


if __name__ == '__main__':
    main()
