f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

bussIds = lines[1].split(",")

step = 0
for bussId in bussIds:
    if (bussId == "x"):
        step += 1
        continue

    remainder = (int(bussId) - step) % int(bussId)
    print("({}, {})".format(remainder, bussId))
    step += 1
