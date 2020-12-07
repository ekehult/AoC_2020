from functools import reduce

f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

class Trees:
    treeCount: int
    movementX: int
    movementY: int
    currentX: int

trees = [
    Trees(0, 1, 1, 0),
    Trees(0, 3, 1, 0),
    Trees(0, 5, 1, 0),
    Trees(0, 7, 1, 0),
    Trees(0, 1, 2, 0)
]
lineNumber = 0

for line in lines:
    for trobo in trees:
        if (lineNumber % trobo.movementY):
            if ("#" == trobo.currentX):
                trobo.treeCount += 1
            trobo.currentX = (trobo.currentX + trobo.movementX) % len(line)
        lineNumber += 1


print(reduce((lambda x, y: x[0] * y[0]), [row.treeCount for row in trees]))