f = open("input.txt", "r")
lines = f.readlines()
lines = [int(x.strip()) for x in lines]


nof_ones = 0
nof_twos = 0
nof_threes = 0

lines.sort()
lines.append(lines[-1]+3)
last = 0
for line in lines: 
    diff = line - last
    if (diff == 1):
        nof_ones += 1
    if (diff == 3):
        nof_threes += 1
    last = line

print(nof_ones)
print(nof_twos)
print(nof_threes)
print(nof_ones*nof_threes)
    