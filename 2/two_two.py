f = open("input.txt", "r")
lines = f.readlines()
lines = [x.split(" ") for x in lines]

valid_pswds = 0

for line in lines:
    min, max = [int(x) for x in line[0].split("-")]
    req_letter = line[1][0]
    if (line[2][min-1] == req_letter) ^  (line[2][max-1] == req_letter):
        valid_pswds += 1
    
print(valid_pswds)
