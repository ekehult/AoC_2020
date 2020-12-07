import re

f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip().split(" ") for x in lines]

class Passport:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    def __init__(self, value):
        self.byr =  value
        self.iyr =  value
        self.eyr =  value
        self.hgt =  value
        self.hcl =  value
        self.ecl =  value
        self.pid =  value

    def validPassport(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

eclSet = {
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
}

currentPassport = Passport(False)
foundNewLine = False
validPassports = 0
for line in lines:
    if (foundNewLine):
        if (currentPassport.validPassport()):
            validPassports += 1
        currentPassport = Passport(False)
        foundNewLine = False

    for elem in line:
        if (elem == ""):
            foundNewLine = True
            break
        print(elem)

        token, value = elem.split(":")
        if (token == "byr"):
            if (1920 <= int(value) and int(value) <= 2002):
                currentPassport.byr = True
        elif (token == "iyr"):
            if (2010 <= int(value) and int(value) <= 2020):
                currentPassport.iyr = True
        elif (token == "eyr"):
            if (2020 <= int(value) and int(value) <= 2030):
                currentPassport.eyr = True
        elif (token == "hgt"):
            if (len(value) > 3):
                height = int(value[:-2])
                unit = value[-2:]
                if (unit == "cm" and 150 <= height and height <= 193):
                    currentPassport.hgt = True
                elif (unit == "in" and 59 <= height and height <= 76):
                    currentPassport.hgt = True
        elif (token == "hcl"):
            if(re.search("^#[0-9a-f]{6}$", value)):
                currentPassport.hcl = True
        elif (token == "ecl"):
            if(value in eclSet):
                currentPassport.ecl = True
        elif (token == "pid"):
            if(len(value) == 9):
                currentPassport.pid = True

if(currentPassport.validPassport()):
    validPassports += 1

print(validPassports)