f = open("input.txt", "r")
instructions = [line.split(' ') for line in f.read().splitlines()]

def isCloseToHead(knot1, knot2):
    allPositions = [[knot2[0], knot2[1]], [knot2[0], knot2[1] + 1], [knot2[0] + 1, knot2[1] + 1], [knot2[0] + 1, knot2[1]], [knot2[0] + 1, knot2[1] - 1], [knot2[0], knot2[1] - 1], [knot2[0] - 1, knot2[1] - 1], [knot2[0] - 1, knot2[1]], [knot2[0] - 1, knot2[1] + 1]]
    return knot1 in allPositions

def moveTail(rope):
    count = 0
    for knot1, knot2 in zip(rope[:-1], rope[1:]):
        count += 1
        if not isCloseToHead(knot1, knot2):
            if knot1[1] == knot2[1]:
                knot2[0] = knot2[0] + 1 if knot1[0] > knot2[0] else knot2[0] - 1
            elif knot1[0] == knot2[0]:
                knot2[1] = knot2[1] + 1 if knot1[1] > knot2[1] else knot2[1] - 1
            elif knot1[0] > knot2[0]:
                knot2[0] += 1
                knot2[1] = knot2[1] + 1 if knot1[1] > knot2[1] else knot2[1] - 1
            elif knot1[0] < knot2[0]:
                knot2[0] -= 1
                knot2[1] = knot2[1] + 1 if knot1[1] > knot2[1] else knot2[1] - 1
        if count == len(rope) - 1:
            visited.add(tuple(knot2))

def followInstructions(rope):
    for inst in instructions:
        for _ in range(int(inst[1])):
            if inst[0] == 'U':
                rope[0][1] += 1
            elif inst[0] == 'D':
                rope[0][1] -= 1
            elif inst[0] == 'L':
                rope[0][0] -= 1
            elif inst[0] == 'R':
                rope[0][0] += 1
            moveTail(rope)
    return len(visited)

visited = set()
visited.add((0, 0))
print('Part 1: ', followInstructions([[0, 0] for _ in range(2)]))
visited.clear()
visited.add((0, 0))
print('Part 2: ', followInstructions([[0, 0] for _ in range(10)]))