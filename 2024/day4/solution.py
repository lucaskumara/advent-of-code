puzzle = []

count = 0


def xmas_search(row_index, column_index, puzzle_height, puzzle_width):
    if puzzle[row_index][column_index] != 'X':
        return 0

    modifiers = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    count = 0

    for modifier in modifiers:
        word = 'X'

        row_modifier, column_modifier = modifier

        for i in range(1, 4):
            new_row_index = row_index + row_modifier * i
            new_column_index = column_index + column_modifier * i

            if new_row_index >= 0 and \
                    new_row_index < puzzle_height and \
                    new_column_index >= 0 and \
                    new_column_index < puzzle_width:
                word += puzzle[new_row_index][new_column_index]

        if word == 'XMAS':
            count += 1

    return count


def x_mas_search(row_index, column_index, puzzle_height, puzzle_width):
    if puzzle[row_index][column_index] != 'A':
        return 0

    if row_index == 0 or row_index == puzzle_height - 1 or \
            column_index == 0 or column_index == puzzle_width - 1:
        return 0

    modifiers = [
        (-1, -1),
        (-1, 1)
    ]

    for modifier in modifiers:
        row_modifer, column_modifier = modifier

        text = f'{puzzle[row_index + row_modifer][column_index + column_modifier]}A{puzzle[row_index - row_modifer][column_index - column_modifier]}'

        if text not in ['MAS', 'SAM']:
            return 0

    return 1


with open('input.txt') as file:
    for line in file:
        puzzle.append(list(line.strip()))

puzzle_height = len(puzzle)
puzzle_width = len(puzzle[0])

for row_index in range(puzzle_height):
    for column_index in range(puzzle_width):
        # count += xmas_search(row_index, column_index, puzzle_height, puzzle_width)  # Part 1
        count += x_mas_search(row_index, column_index, puzzle_height, puzzle_width) # Part 2


print(count)