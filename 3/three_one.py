f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]


trees = [
    [0, 1, 1, 0],
    [0, 3, 1, 0],
    [0, 5, 1, 0],
    [0, 7, 1, 0],
    [0, 1, 2, 0]
]
# 1, 1
xPosOne = 0
# 3, 1
xPosTwo = 0
# 5, 1
xPosThree = 0
# 7, 1
xPosFour = 0
# 1, 2
xPosFive = 0

lineNumber = 0

treesOne = 0
treesTwo = 0
treesThree = 0
treesFour = 0
treesFive = 0
for line in lines:
    if ("#" == line[xPosOne]):
        treesOne += 1
    if ("#" == line[xPosTwo]):
        treesTwo += 1
    if ("#" == line[xPosThree]):
        treesThree += 1
    if ("#" == line[xPosFour]):
        treesFour += 1
    if (lineNumber % 2 == 0):
        if ("#" == line[xPosFive]):
            treesFive += 1
        xPosFive = (xPosFive + 1) % len(line)

    xPosOne = (xPosOne + 1) % len(line)
    xPosTwo = (xPosTwo + 3) % len(line)
    xPosThree = (xPosThree + 5) % len(line)
    xPosFour = (xPosFour + 7) % len(line)

    lineNumber += 1

print(treesOne * treesTwo * treesThree * treesFour * treesFive)