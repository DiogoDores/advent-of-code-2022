f = open("input.txt", "r")
forest = [[int(num) for num in line.strip()] for line in f]
visibleTrees = len(forest) * 2 + len(forest[0]) * 2 - 4
visible = set()
scenicViews = []

def findVisibleTrees(horizontal = True):
    for y in range(1, len(forest) - 1):
        highestTree = forest[y][0] if horizontal else forest[0][y]
        for x in range(1, len(forest[0]) - 1):
            if horizontal and forest[y][x] > highestTree:
                highestTree = forest[y][x]
                visible.add((y, x))
            elif not horizontal and forest[x][y] > highestTree:
                highestTree = forest[x][y]
                visible.add((x, y))

def findVisibleTreesReversed(horizontal = True):
    for y in reversed(range(1, len(forest) - 1)):
        highestTree = forest[y][len(forest) - 1] if horizontal else forest[len(forest) - 1][y]
        for x in reversed(range(1, len(forest[0]) - 1)):
            if horizontal and forest[y][x] > highestTree:
                highestTree = forest[y][x]
                visible.add((y, x))
            elif not horizontal and forest[x][y] > highestTree:
                highestTree = forest[x][y]
                visible.add((x, y))

def getLineOfSight(i, j, trees):
    treesInSight = 0
    for tree in trees:
        treesInSight += 1
        if tree >= forest[i][j]:
            break
    return treesInSight

findVisibleTrees()
findVisibleTrees(False)
findVisibleTreesReversed()
findVisibleTreesReversed(False)

for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[i]) - 1):
        up = getLineOfSight(i, j, [forest[x][j] for x in reversed(range(i))])
        down = getLineOfSight(i, j, [forest[x][j] for x in range(i + 1, len(forest))])
        left = getLineOfSight(i, j, [forest[i][x] for x in reversed(range(j))])
        right = getLineOfSight(i, j, [forest[i][x] for x in range(j + 1, len(forest[j]))])

        scenicViews.append(up * down * left * right)

print('Part 1: ', len(visible) + visibleTrees)
print('Part 2: ', max(scenicViews))