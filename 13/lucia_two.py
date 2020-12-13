f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

bussIds = lines[1].split(",")

def stepMatches(t, id):
    rest = t % id
    return rest == 0

def matchesInPattern(t, ids):
    if (len(ids) < 1):
        return True

    token = ids[0]
    if (token == "x"):
        return matchesInPattern(t + 1, ids[1:])

    return (stepMatches(t, int(token)) and matchesInPattern(t + 1, ids[1:]))


firstBusId = int(bussIds[0])
startingT = firstBusId
while(True):
    if(matchesInPattern(startingT + 1, bussIds[1:])):
        print("### STARTING T: {}".format(startingT))
        break
    startingT += firstBusId