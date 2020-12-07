f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

ids = []
for line in lines:
    row = line[:7]
    col = line[7:]
    rowNumber = ""
    for elem in row:
        rowNumber += "1" if elem == "B" else "0"
    colNumber = ""
    for elem in col:
        colNumber += "1" if elem == "R" else "0"

    seatId = int(rowNumber, 2) * 8 + int(colNumber, 2)
    ids.append(seatId)

ids.sort()
print(ids)

lastID = ids[0]
for id in ids[1:]:
    shouldBeNextID = int(lastID) + 1
    if (shouldBeNextID != int(id)):
        print(shouldBeNextID)
        # break
    lastID = id


