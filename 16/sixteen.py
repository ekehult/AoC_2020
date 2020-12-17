f = open("manipulated_input.txt", "r")
lines = f.readlines()
lines = [x.strip().split(":") for x in lines]

readingRules = True
rules = {}

def parseInterval(interval):
    first, second = interval.split("-")
    return (int(first), int(second))

def addRule(name, firstInterval, secondInterval):
    rules[name] = (parseInterval(firstInterval), parseInterval(secondInterval))

def checkRule(number, interval):
    start, stop = interval
    return start <= number and number <= stop

def checkValue(number):
    for firstInterval, secondInterval in rules.values():
        if(checkRule(number, firstInterval) or checkRule(number, secondInterval)):
            return True
    return False

validTickets = []

sum = 0
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
        for number in line[0].split(","):
            if(not checkValue(int(number))):
                sum += int(number)

print(sum)