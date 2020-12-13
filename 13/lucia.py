f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

arrivingTime = int(lines[0])

ids = lines[1].split(",")

def calcArrivalTime(id):
    sum = id
    while sum < arrivingTime:
        sum += id
    return sum 


busArrivalTimes = []
for id in ids:
    if (id == "x"):
        continue
    arrivalTime = calcArrivalTime(int(id))
    busArrivalTimes.append((int(id), arrivalTime))

busArrivalTimes.sort(key = lambda tup: tup[1])

print(busArrivalTimes)

print((busArrivalTimes[0][1] - arrivingTime) * busArrivalTimes[0][0])