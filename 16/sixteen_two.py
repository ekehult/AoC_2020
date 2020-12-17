import re

f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip().split(":") for x in lines]

rules = {}

def parseInterval(interval):
    first, second = interval.split("-")
    return (int(first), int(second))

def addRule(name, firstInterval, secondInterval):
    rules[name] = (parseInterval(firstInterval), parseInterval(secondInterval))

def checkRule(number, interval):
    start, stop = interval
    return start <= number and number <= stop

def checkValue(rule, number):
    firstInterval, secondInterval = rules[rule]
    if(checkRule(number, firstInterval) or checkRule(number, secondInterval)):
        return True
    return False

def matchesAnyRule(number):
    for rule in rules.keys():
        if(checkValue(rule, number)):
            return True
    return False


def validTicket(numbers):
    for number in numbers:
        if(not matchesAnyRule(number)):
            return False
    return True


validTickets = []
readingRules = True
readOurTicket = False
ourTicket = []
for line in lines:
    if (line[0] == ""):
        readingRules = False
        continue

    if (readingRules):
        name = line[0]
        intervals = line[1].strip().split(" ")
        firstInterval = intervals[0]
        secondInterval = intervals[2]

        addRule(name, firstInterval, secondInterval)
    else:
        ticketNumbers = [int(x) for x in line[0].split(",")]
        if (not readOurTicket):
            ourTicket = ticketNumbers
            readOurTicket = True
        if(validTicket(ticketNumbers)):
            validTickets.append(ticketNumbers)


def checkColumnForRule(rule, column):
    firstInterval, secondInterval = rules[rule]
    for number in column:
        if (not checkValue(rule, number)):
            return False
    return True


numberOfColumns = len(validTickets[0])
pairing = {}
for rule in rules.keys():
    pairing[rule] = [0] * numberOfColumns

for i in range(numberOfColumns):
    column = [x[i] for x in validTickets]
    for rule in rules.keys():
        if (checkColumnForRule(rule, column)):
            pairing[rule][i] = 1


def findIndexOfOne(rows):
    for i in range(len(rows)):
        if (rows[i] == 1):
            return i
    return -1

def zeroIndexInAllPairings(index):
    for columns in pairing.values():
        columns[index] = 0

def containsDeparture(name):
    if(re.search("^departure", name)):
        return True
    return False


foundPairings = 0
productOfDepartureValues = 1
while(foundPairings < len(pairing)):
    for rule, row in pairing.items():
        if (sum(row) == 1):
            index = findIndexOfOne(row)
            zeroIndexInAllPairings(index)
            print("Rule: '{}', Column index: {}".format(rule, index))
            foundPairings += 1
            if (containsDeparture(rule)):
                productOfDepartureValues *= ourTicket[index]


print(productOfDepartureValues)
            