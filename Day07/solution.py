from collections import defaultdict
f = open("input.txt", "r")
directory = [line.strip() for line in f]
sizes = defaultdict(int)
stack = []

for file in directory:
    match file.split():
        case [_, _, '/']:
            stack = []
        case [_, _, '..']:
            stack.pop()
        case [_, _, x]:
            stack.append(x)
        case [x, _]:
            if x.isdigit():
                for i in range(len(stack) + 1):
                    path = "/" + "/".join(stack[:i])
                    sizes[path] += int(x)

neededSpace = 30000000 - (70000000 - sizes['/'])
print('Part 1: ', sum(filter(lambda x: x <= 100000, sizes.values())))
print('Part 2: ', min((dict((k,v) for k, v in sizes.items() if v > neededSpace)).values()))