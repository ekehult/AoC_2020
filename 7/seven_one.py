visitedNodes = set()
bagRelationships = dict()

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def recursiveSearch(parents):
    for parent in parents:
        if (parent in visitedNodes):
            continue

        visitedNodes.add(parent)
        if (parent in bagRelationships):
            recursiveSearch(bagRelationships[parent])


f = open("test.txt", "r")
lines = f.readlines()
lines = [x.strip() for x in lines]


for line in lines:
    parentName, children = [x.strip() for x in line.split("bags contain")]

    children = [x.split() for x in children.split(",")]
    
    for child in children:
        if(RepresentsInt(child[0])):
            childName = child[1] + " " + child[2]
            if (childName in bagRelationships):
                bagRelationships[childName].append(parentName)
            else:
                bagRelationships[childName] = [parentName]

# print(bagRelationships)
recursiveSearch(bagRelationships["shiny gold"])
print(len(visitedNodes))