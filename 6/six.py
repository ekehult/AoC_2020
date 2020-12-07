f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

foundBlankLine = False
customsCheck = set()
sum = 0
for line in lines:
    if (foundBlankLine):
        foundBlankLine = False
        sum += len(customsCheck)
        customsCheck = set()

    if (len(line) == 0):
        foundBlankLine = True
        continue

    for elem in line:
        customsCheck.add(elem)

sum += len(customsCheck)

print(sum)