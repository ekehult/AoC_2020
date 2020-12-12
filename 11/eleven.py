f = open("input.txt", "r")
lines = f.readlines()
lines = [list(x.strip()) for x in lines]

max_y = len(lines)
max_x = len(lines[0])

def getPosition(x, y):
    if (x >= 0 and x < max_x and y >= 0 and y < max_y):
        return lines[y][x]
    return (".")

def getAdjacent(x, y):
    adjacentSeats = []
    for col in range(x-1,x+2):
        for row in range(y-1,y+2):
            adjacentSeats.append(getPosition(col, row))
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