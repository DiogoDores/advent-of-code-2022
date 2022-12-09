f = open("example.txt", "r")
instructions = [line.split(' ') for line in f.read().splitlines()]
rope = {'H': [0, 0], 'T': [0, 0]}
visited = set()
visited.add((0, 0))

def isSameColOrRow():
    return rope['T'][0] == rope['H'][0] or rope['T'][1] == rope['H'][1]

def isCloseToHead():
    top = rope['T'][0] + 1
    return 

for inst in instructions:
    oldHeadPos = rope['H']
    for step in range(int(inst[1])):
        if inst[0] == 'U':
            rope['H'][1] += 1
            if isSameColOrRow():
                rope['T'][1] += 1
            else:
                rope['T'] = oldHeadPos
        elif inst[0] == 'D':
            rope['H'][1] -= 1
            if isSameColOrRow():
                rope['T'][1] -= 1
            else:
                rope['T'] = oldHeadPos
        elif inst[0] == 'L':
            rope['H'][0] -= 1
            if isSameColOrRow():
                rope['T'][0] -= 1
            else:
                rope['T'] = oldHeadPos
        elif inst[0] == 'R':
            rope['H'][0] += 1
            if isSameColOrRow():
                rope['T'][0] += 1
            else:
                rope['T'] = oldHeadPos
        print(rope['H'], '|', rope['T'])
    visited.add(tuple(rope['T']))
    
    
print(visited)