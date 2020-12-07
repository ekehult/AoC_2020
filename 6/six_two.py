f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

foundBlankLine = False
newGroup = True
groupCustoms = set()
sum = 0
for line in lines:
    if (foundBlankLine):
        newGroup = True
        foundBlankLine = False
        sum += len(groupCustoms)
        groupCustoms = set()

    if (len(line) == 0):
        foundBlankLine = True
        continue

    if (newGroup):
        newGroup = False
        groupCustoms = set([char for char in line])
    else:
        lineCustoms = set([char for char in line])
        groupCustoms = groupCustoms.intersection(lineCustoms)


sum += len(groupCustoms)

print(sum)