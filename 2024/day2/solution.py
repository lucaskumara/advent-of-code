part1_counter = 0
part2_counter = 0

def is_safe(levels):
    higher = 0

    for i in range(len(levels) - 1):
        if levels[i] + 1 <= levels[i + 1] <= levels[i] + 3:
            higher += 1
        elif levels[i] - 1 >= levels[i + 1] >= levels[i] - 3:
            higher -= 1
        
    return abs(higher) == len(levels) - 1

with open('input.txt') as file:
    for report in file:
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            part1_counter += 1
            part2_counter += 1
        else:
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i + 1:]

                if is_safe(modified_levels):
                    part2_counter += 1
                    break

print(part1_counter)
print(part2_counter)