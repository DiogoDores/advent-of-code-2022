f = open("input.txt", "r")
rounds = [[line[0], line[2]] for line in f.readlines()]
pointsP1, pointsP2 = 0, 0

# ROCK - A and X
# PAPER - B and Y
# SCISSORS - C and Z

for round in rounds:
    if round[1] == 'X':
        pointsP1 += 1
        if round[0] == 'C': #WIN
            pointsP1 += 6
        elif round[0] == 'A': #TIE
            pointsP1 += 3
    elif round[1] == 'Y':
        pointsP1 += 2
        if round[0] == 'A': #WIN
            pointsP1 += 6
        elif round[0] == 'B': #TIE
            pointsP1 += 3
    elif round[1] == 'Z':
        pointsP1 += 3
        if round[0] == 'B': #WIN
            pointsP1 += 6
        elif round[0] == 'C': #TIE
            pointsP1 += 3

for round in rounds:
    if round[0] == 'A': #ROCK
        if round[1] == 'X': #SCISSORS
            pointsP2 += 3
        elif round[1] == 'Y': #ROCK
            pointsP2 += 4
        elif round[1] == 'Z': #PAPER
            pointsP2 += 8
    elif round[0] == 'B': #PAPER
        if round[1] == 'X': #ROCK
            pointsP2 += 1
        elif round[1] == 'Y': #PAPER
            pointsP2 += 5
        elif round[1] == 'Z': #SCISSORS
            pointsP2 += 9
    elif round[0] == 'C': #SCISSORS
        if round[1] == 'X': #PAPER
            pointsP2 += 2
        elif round[1] == 'Y': #SCISSORS
            pointsP2 += 6
        elif round[1] == 'Z': #ROCK
            pointsP2 += 7

print("Part 1: ", pointsP1)
print("Part 2: ", pointsP2)
