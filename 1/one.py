import sys

f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]

count = 1
for base in lines:
    for test1 in lines[count:]:
        for test2 in lines[count + 1:]:
            sum = int(base) + int(test1) + int(test2)
            if (sum == 2020):
                print("End value {}".format(int(base) * int(test1) * int(test2)))
                sys.exit(0)
    count += 1



