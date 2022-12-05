import copy
f = open("input.txt", "r")
cargo, instructions = f.read().split('\n\n')
orderedCargo = [[] for _ in range(-(len(cargo.split('\n')[0])//-4))]

for row in cargo.split('\n'):
    for c in range(len(row)):
        if row[c].isalpha():
            orderedCargo[c//4].append(row[c])

cargoP1, cargoP2 = copy.deepcopy(orderedCargo), copy.deepcopy(orderedCargo)
for inst in instructions.split('\n'):
    instList = inst.split(' ')
    n, fro, to = int(instList[1]), int(instList[3]), int(instList[5])
    for _ in range(n):
        cargoP1[to - 1].insert(0, cargoP1[fro - 1].pop(0))
    for i in reversed(range(n)):
        cargoP2[to - 1].insert(0, cargoP2[fro - 1].pop(i))

print('Part 1: ', ''.join(item[0] for item in cargoP1))
print('Part 2: ', ''.join(item[0] for item in cargoP2))