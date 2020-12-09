f = open("input.txt", "r")
lines = f.readlines()
lines = [int(x.strip()) for x in lines]

def isValid(numbersBefore, expectedSum):
    index = 0
    testSum = numbersBefore[0]
    for number in numbersBefore[1:]:
        index += 1
        testSum += number
        if (testSum == expectedSum):
            return (True, index)
        if (testSum > expectedSum):
            return (False, 0)

    return (False, 0)

def createOutput(numbers):
    numbers.sort()
    sum = numbers[0] + numbers[-1]
    print("#### Answer ####")
    print(sum)


expectedSum = 177777905
currentIndex = 0
while(currentIndex < len(lines)):
    numbersToCheck = lines[currentIndex:]
    passed, relativeIndex = isValid(numbersToCheck, expectedSum)
    if (passed):
        createOutput(lines[currentIndex:currentIndex + relativeIndex])
        break
    else:
        currentIndex += 1