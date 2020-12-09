f = open("input.txt", "r")
lines = f.readlines()
lines = [int(x.strip()) for x in lines]

def isValid(numbersBefore, expectedSum):
    index = 0
    while(index < len(numbersBefore)):
        number = numbersBefore[index]
        index += 1
        for testNumber in numbersBefore[index:]:
            testSum = testNumber + number
            if (testSum == expectedSum):
                return True

    return False


window = 25
currentIndex = 25
while(currentIndex < len(lines)):
    expectedSum = lines[currentIndex]
    numbersToCheck = lines[currentIndex - window: currentIndex]
    if (isValid(numbersToCheck, expectedSum)):
        currentIndex += 1
    else:
        print(expectedSum)
        break