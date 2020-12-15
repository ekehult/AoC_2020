f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip().split(",") for x in lines]

startingNumbers = lines[0]
spokenNumbers = {}

for x in range(len(startingNumbers)):
    spokenNumbers[int(startingNumbers[x])] = [x + 1]

lastNumber = int(startingNumbers[-1])

def addToSpokenNumbers(number, i):        
    if (number in spokenNumbers):
        spokenNumbers[number].append(i)
    else:
        spokenNumbers[number] = [i]


start = len(startingNumbers) + 1
end =  30000000 + 1
for i in range(start, end):
    if (len(spokenNumbers[lastNumber]) < 2):
        addToSpokenNumbers(0, i)
        lastNumber = 0

    else:
        lastTwoOccurences = spokenNumbers[lastNumber][-2:]
        diff = lastTwoOccurences[1] - lastTwoOccurences[0]
        addToSpokenNumbers(diff, i)
        lastNumber = diff


print(lastNumber)