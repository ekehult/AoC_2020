bagRelationships = dict()

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def recursiveSearch(children):
    sum = 0
    for childTuple in children:
        childName, count = childTuple

        sum += count
        if (childName in bagRelationships):
            sum += count * recursiveSearch(bagRelationships[childName])

    return sum


        

f = open("input.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]


for line in lines:
    parent, children = [x.strip() for x in line.split("bags contain")]

    children = [x.split() for x in children.split(",")]
    childArray = []
    
    for child in children:
        if(RepresentsInt(child[0])):
            childName = child[1] + " " + child[2]
            childArray.append((childName, int(child[0])))

            
    bagRelationships[parent] = childArray

print(recursiveSearch(bagRelationships["shiny gold"]))