f = open("input.txt", "r")
instructions = [line.split(' ') for line in f.read().splitlines()]
rope = {'H': [0, 0], 'T': [0, 0]}
visited = set()
visited.add((0, 0))

def isSameColOrRow():
    return rope['T'][0] == rope['H'][0] or rope['T'][1] == rope['H'][1]

def isCloseToHead():
    tail = rope['T']
    allPositions = [[tail[0], tail[1]], [tail[0], tail[1] + 1], [tail[0] + 1, tail[1] + 1], [tail[0] + 1, tail[1]], [tail[0] + 1, tail[1] - 1], [tail[0], tail[1] - 1], [tail[0] - 1, tail[1] - 1], [tail[0] - 1, tail[1]], [tail[0] - 1, tail[1] + 1]]
    return rope['H'] in allPositions

def moveTail():
    if not isCloseToHead():
        if rope['H'][1] == rope['T'][1]:
            rope['T'][0] = rope['T'][0] + 1 if rope['H'][0] > rope['T'][0] else rope['T'][0] - 1
        elif rope['H'][0] == rope['T'][0]:
            rope['T'][1] = rope['T'][1] + 1 if rope['H'][1] > rope['T'][1] else rope['T'][1] - 1
        elif rope['H'][0] > rope['T'][0]:
            rope['T'][0] += 1
            rope['T'][1] = rope['T'][1] + 1 if rope['H'][1] > rope['T'][1] else rope['T'][1] - 1
        elif rope['H'][0] < rope['T'][0]:
            rope['T'][0] -= 1
            rope['T'][1] = rope['T'][1] + 1 if rope['H'][1] > rope['T'][1] else rope['T'][1] - 1            

for inst in instructions:
    for step in range(int(inst[1])):
        if inst[0] == 'U':
            rope['H'][1] += 1
        elif inst[0] == 'D':
            rope['H'][1] -= 1
        elif inst[0] == 'L':
            rope['H'][0] -= 1
        elif inst[0] == 'R':
            rope['H'][0] += 1
        moveTail()
        visited.add(tuple(rope['T']))
        print(rope['H'], '|', rope['T'])
    
    
print(len(visited))