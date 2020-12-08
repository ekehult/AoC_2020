f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip().split(" ") for x in lines]


visitedRows = set()
indexVisited = []
lastRewindLength = len(lines)
accumulator = 0
index = 0

def rewind():
    global index, accumulator, visitedRows, indexVisited, lastRewindLength

    print("#### REWIND ####")
    while (len(indexVisited)):
        index = indexVisited.pop()
        visitedRows.remove(str(index))
        operation, parameter = lines[index]

        print("operation: " + operation)
        print("parameter: " + parameter)
        print("index: " + str(index))


        if (operation == "acc"):
            accumulator -= int(parameter)
            continue

        if (len(indexVisited) < lastRewindLength):
            lastRewindLength = len(indexVisited)
            print("#### END ####")
            return
    

while (index < len(lines)):
    changeOp = False
    if (str(index) in visitedRows):
        rewind()
        changeOp = True

    visitedRows.add(str(index))
    operation, parameter = lines[index]
    if (changeOp):
        operation = "nop" if operation == "jmp" else "jmp"
    indexVisited.append(index)
    print("operation: " + operation)
    print("parameter: " + parameter)
    print("index: " + str(index))

    if (operation == "acc"):
        accumulator = accumulator + int(parameter)
    elif (operation == "jmp"):
        index = index + int(parameter)
        continue
    index += 1

print(accumulator)