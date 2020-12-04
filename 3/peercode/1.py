from copy import deepcopy
 
lines = [line.strip() for line in open('../input.txt') if line]
orig = []
 
for row, line in enumerate(lines):
    orig.append([])
    for i, c in enumerate(line):
        orig[row].append(c)
 
def checkFor(xStep, yStep):
    y, x = 0, 0
    treeCount = 0
    box = deepcopy(orig)
    while y < len(box):
        if box[y][x] == '#': 
            treeCount += 1
 
        x += xStep
        y += yStep
 
        if x >= len(box[0]): x -= len(box[0])
    return treeCount
 
part1 = checkFor(3,1)
a = checkFor(1,1)
b = checkFor(3,1)
c = checkFor(5,1)
d = checkFor(7,1)
e = checkFor(1,2)
part2 = a * b * c * d * e
print('part1:', part1)
print('part2:', part2)