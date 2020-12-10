f = open("input.txt", "r")
lines = f.readlines()
lines = [int(x.strip()) for x in lines]

def permutationScore(length):
	if (length == 3):
		return 2
	if (length == 4):
		return 4
	if (length == 5):
		return 7

	return 1

inSequence = False
sequenceStart = 0
sequenceEnd = 0
sum = 1
lines.append(0)
lines.sort()
lines.append(lines[-1]+3)
index = 0

while(index < len(lines) - 1):
	diff = lines[index + 1] - lines[index]
	if (inSequence):
		if (diff == 3):
			sequenceEnd = index + 1
			inSequence = False
			print(sequenceEnd - sequenceStart)
			print(lines[sequenceStart:sequenceEnd])
			sum = sum * permutationScore(sequenceEnd - sequenceStart)
	else:
		if (diff == 1):
			sequenceStart = index
			inSequence = True

	index += 1

print sum