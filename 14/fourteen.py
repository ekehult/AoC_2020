f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip().split(" ") for x in lines]

mask = ""
memory = {}

def parseMemmoryAddress(token):
    return token[4:-1]

def maskValue(value):
    binaryRepresentation = "{0:b}".format(value).zfill(36)

    maskedValue = ""
    for i in range(len(mask)):
        if (mask[i] == "1"):
            maskedValue += "1"
        elif (mask[i] == "0"):
            maskedValue += "0"
        else:
            maskedValue += binaryRepresentation[i]

    return maskedValue

for line in lines:
    token, operator, value = line
    if (token == "mask"):
        mask = value
        continue
    memory[parseMemmoryAddress(token)] = maskValue(int(value))


print(sum([int(value, 2) for value in memory.values()]))