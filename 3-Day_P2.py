"""
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123
specifies a rectangle 3 inches from the left edge, 2 inches from
the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims
to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2.
(Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will
have enough fabric. How many square inches of fabric are within two or
more claims?
"""

inputFile = open('3-Input.txt', 'r')
count = len(open('3-Input.txt').readlines(  ))
lines = ["" for x in range(count)]
box = [0 for x in range(1000000)] #1000x1000 Box to fill with counts per space
afterA = ""
distIn = ""
distDown = ""
overlapCt = 0
for x in range(count):
    lines[x] = inputFile.readline().strip()

# #2 @ 3,1: 4x4

for x in range(count):
    #print(x, end =" ")
    currLine = lines[x]
    lineLen = len(currLine)
    #print(currLine)
    #X-Axis
    #Find @
    for l in range(lineLen):
        if(currLine[l] == "@"):
            aLoc = l
            #print(aLoc)
            
    for l in range(lineLen):
        if(currLine[l] == ","):
            commaLoc = l
            #print(commaLoc)

    #Find Dimensins 
    for l in range(lineLen):
        if(currLine[l] == ":"):
            colinLoc = l
            #print(colinLoc)

    #Find DistDown 
    for l in range(lineLen):
        if(currLine[l] == "x"):
            xLoc = l
            #print(xLoc)
            
    #Find DistIn
    for l in range(lineLen):
        if(currLine[l] == ","):
            comLoc = l
            #print(comLoc)

    distIn = int(currLine[(aLoc+2):(commaLoc)])
    #print(distIn)
    distDown = int(currLine[(commaLoc+1):colinLoc])
    #print(distDown)
    width =  int(currLine[(colinLoc+2):xLoc])
    #print(width)
    height = int(currLine[(xLoc+1):])
    #print(height)

    for y in range(height):
        for x in range(width):
            box[((distDown*1000)+distIn+x)] += 1
        distDown += 1
        #print(distDown)

overlapCt = 0

for x in range(1000000):
    if(int(box[x]) >= 2):
        overlapCt += 1
    #print((box[x]), end =" ")
#print(box)

print(overlapCt)

boxId = 0
x = 0
for m in range(count):
    #print(x, end =" ")
    currLine = lines[m]
    lineLen = len(currLine)
    #print(currLine)
    #X-Axis
    #Find @
    for l in range(lineLen):
        if(currLine[l] == "@"):
            aLoc = l
            #print(aLoc)
            
    for l in range(lineLen):
        if(currLine[l] == ","):
            commaLoc = l
            #print(commaLoc)

    #Find Dimensins 
    for l in range(lineLen):
        if(currLine[l] == ":"):
            colinLoc = l
            #print(colinLoc)

    #Find DistDown 
    for l in range(lineLen):
        if(currLine[l] == "x"):
            xLoc = l
            #print(xLoc)
            
    #Find DistIn
    for l in range(lineLen):
        if(currLine[l] == ","):
            comLoc = l
            #print(comLoc)

    #print(currLine)
    #print(aLoc)
    boxId = int(currLine[(1):(aLoc-1)])
    #print(boxId)
    distIn = int(currLine[(aLoc+2):(commaLoc)])
    #print(distIn)
    distDown = int(currLine[(commaLoc+1):colinLoc])
    #print(distDown)
    width =  int(currLine[(colinLoc+2):xLoc])
    #print(width)
    height = int(currLine[(xLoc+1):])
    #print(height)

    x = 0
    y = 0
    thisIsBox = True
    for y in range(height):
        for x in range(width):
            if(box[((distDown*1000)+distIn+x)] != 1):   
                thisIsBox = False
        distDown += 1
    if(thisIsBox == True):
        print("The Answer Is:")
        print(boxId)
        #print(distDown)


    

























    
