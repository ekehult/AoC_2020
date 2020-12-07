import sys

f = open("input.txt", "r")
lines = f.readlines()
lines = [x.split(" ") for x in lines]

valid_pswds = 0

for line in lines:
    min, max = [int(x) for x in line[0].split("-")]
    req_letter = line[1][0]
    counter = 0
    for letter in line[2]:
        if letter == req_letter:
            counter +=1
            if counter > max:
                break
    if min <= counter and counter <= max:
        valid_pswds += 1
    
print(valid_pswds)
