f = open("input.txt", "r")
lines = f.readlines()
lines = [list(x.strip()) for x in lines]

max_y = len(lines)
max_x = len(lines[0])

def getPosition(x, y, xDir, yDir):
    x += xDir
    y += yDir
    while(x >= 0 and x < max_x and y >= 0 and y < max_y):
        seat = lines[y][x]
        if (seat != "."):
            return seat
        x += xDir
        y += yDir
    return (".")

def getAdjacent(x, y):
    adjacentSeats = []
   # if(y == 1 and x == 0):
       # print("------ POSITION: ({}, {})".format(y, x))
    for xDir in range(-1, 2):
        for yDir in range(-1, 2):
            if (xDir == 0 and yDir == 0):
                continue
            position = getPosition(x, y, xDir, yDir)
            #if(y == 1 and x == 0):
            #    print("({}, {}) = {}".format(row, col, position))
            adjacentSeats.append(position)

    return adjacentSeats


def emptyToOccupied(adjacentSeats):
    if ("#" in adjacentSeats):
        return False
    return True


def occupiedToEmpty(adjacentSeats):
    count = occupiedSeats(adjacentSeats)
    if (count > 4):
        return True
    return False

def occupiedSeats(line):
    return sum(map(lambda x: x == "#", line))

oldChangeLists = []
changeList = []
while(not (changeList in oldChangeLists[-2:])):
    for change in changeList:
        symbol, row, col = change
        lines[row][col] = symbol

    # print("#### NEW STATE ####") 
    # for line in lines:
    #     print(line)
    oldChangeLists.append(changeList)
    changeList = []

    for row in range(max_y):
        for col in range(max_x):
            seat = lines[row][col]
            adjacentSeats = getAdjacent(col, row)
            if (seat == "L" and emptyToOccupied(adjacentSeats)):
                changeList.append(["#", row, col])
            elif (seat == "#" and occupiedToEmpty(adjacentSeats)):
                changeList.append(["L", row, col])


print(sum(map(occupiedSeats, lines)))