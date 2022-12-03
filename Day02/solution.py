f = open("input.txt", "r")
rounds = ["".join(line.split()) for line in f.readlines()]
game1 = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
game2 = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
pointsP1, pointsP2 = 0, 0

for round in rounds:
    pointsP1 += game1.get(round)
    pointsP2 += game2.get(round)

print("Part 1: ", pointsP1)
print("Part 2: ", pointsP2)
