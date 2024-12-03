import re

total = 0


def scan_for_instructions(text, part2=False):
    matches = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", text)

    output = []
    enabled = True and part2

    for instruction in matches:
        if instruction == 'do()':
            enabled = True
        elif instruction == 'don\'t()':
            enabled = False
        else:
            if enabled or not part2:
                left, right = instruction.split(',')

                left_int = int(left.lstrip('mul('))
                right_int = int(right.rstrip(')'))

                output.append((left_int, right_int))

    return output


with open('input.txt') as file:
    instructions = scan_for_instructions(file.read(), part2=True)   # Toggle for part 2

    for instruction in instructions:
        total += instruction[0] * instruction[1]

print(total)