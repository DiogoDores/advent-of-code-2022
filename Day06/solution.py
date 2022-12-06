f = open("input.txt", "r")
datastream = f.read()

def findMarker(window):
    allStrings = [datastream[i:i + window] for i in range(len(datastream) - 2) if len(set(datastream[i:i+window])) == len(datastream[i:i+window])][0]
    return datastream.find(allStrings) + window

print('Part 1: ', findMarker(4))
print('Part 2: ', findMarker(14))