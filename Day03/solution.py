f = open("input.txt", "r")
rucksacks = [line.strip() for line in f]
duplicateItems, badges = [], []

def getPriority(letter):
    return ord(letter) - 38 if letter.isupper() else ord(letter) - 96

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

for items in rucksacks:
    duplicateItems.append(''.join(set(items[:len(items)//2]) & set(items[len(items)//2:])))

for elves in chunker(rucksacks, 3):
    badges.append(''.join(set(elves[0]) & set(elves[1]) & set(elves[2])))

print('Part 1: ', sum(map(getPriority, duplicateItems)))
print('Part 2: ', sum(map(getPriority, badges)))