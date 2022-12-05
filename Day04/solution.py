f = open("input.txt", "r")
pairs = [line.split(',') for line in f.read().splitlines()]
contains, overlaps = 0, 0

for pair in pairs:
    x1, x2 = map(int, pair[0].split('-'))
    y1, y2 = map(int, pair[1].split('-'))
    if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2):
        contains += 1
        overlaps += 1
    elif y1 in range(x1, x2) or y2 in range(x1, x2) or x1 in range(y1, y2) or x2 in range(y1, y2):
        overlaps += 1

print('Part 1:', contains)
print('Part 2:', overlaps)
