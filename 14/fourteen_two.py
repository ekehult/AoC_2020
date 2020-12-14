f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip().split(" ") for x in lines]

memory = {}

def parseMemmoryAddress(token):
    return int(token[4:-1])

def populateMemoryMasks(prefix, remainder):
    if (len(remainder) < 1):
        targetAddresses.append(prefix)
        return
    
    currentBit = remainder[0]
    if(currentBit == "0"):
        return populateMemoryMasks(prefix + "0", remainder[1:])
    elif(currentBit == "1"):
        return populateMemoryMasks(prefix + "1", remainder[1:])

    populateMemoryMasks(prefix + "0", remainder[1:])
    populateMemoryMasks(prefix + "1", remainder[1:])

def maskValue(mask, value):
    binaryRepresentation = "{0:b}".format(value).zfill(36)

    maskedValue = ""
    for i in range(len(mask)):
        if (mask[i] == "1"):
            maskedValue += "1"
        elif(mask[i] == "X"):
            maskedValue += "X"
        else:
            maskedValue += binaryRepresentation[i]

    return maskedValue

currentMask = ""
for line in lines:
    token, operator, value = line
    if (token == "mask"):
        currentMask = value
        continue

    targetAddress = parseMemmoryAddress(token)
    maskedAddress = maskValue(currentMask, targetAddress)
    targetAddresses = []
    populateMemoryMasks("", maskedAddress)

    for address in targetAddresses:
        memory[address] = int(value)


print(sum([int(value) for value in memory.values()]))