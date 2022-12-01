f = open("input.txt", "r")
caloriesPerElf = []
calorieSum = 0

# Part 1
for line in f.readlines():
    if line.strip():
        calorieSum += int(line)
    else:
        caloriesPerElf.append(calorieSum)
        calorieSum = 0

caloriesPerElf.append(calorieSum)
print("Part 1: ", max(caloriesPerElf))

# Part 2
caloriesPerElf.sort(reverse=True)
print("Part 2: ", sum(caloriesPerElf[:3]))