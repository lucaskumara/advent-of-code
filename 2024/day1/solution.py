### Part 1

left_list = []
right_list = []

total = 0

# Load all values into the lists
with open('input.txt') as file:
    for line in file:
        left, right = line.split()

        left_list.append(int(left))
        right_list.append(int(right))

# Sort lists
left_list.sort()
right_list.sort()

# Calculate absolute value for each pair by index (lists are same length)
for i in range(len(left_list)):
    total += abs(left_list[i] - right_list[i])

print(total)


### Part 2

right_counts = {}

score = 0

# Count occurrences in right list
for number in right_list:
    if number in right_counts:
        right_counts[number] += 1
    else:
        right_counts[number] = 1

# Calculate score by iterating through the set and multiplying by the count
for number in left_list:
    if number in right_counts:
        score += number * right_counts[number]

print(score)