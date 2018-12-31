inputFile = open('2-Input.txt', 'r')

count = len(open('2-Input.txt').readlines(  ))
line = ["" for x in range(count)]
currLine = ""
currLetter = ''
compareLetter = ''
matchCount = 0
index = 0
answer = 1
twoCounter = 0
threeCounter = 0
twoFound = 0
threeFound = 0

for x in range(count):
    line[x] = inputFile.readline().strip()
    currLine = line[x]
    #print(currLine)
    length = len(currLine)

    for i in range(length):
        currLetter = currLine[i]
        
        for k in range(length):
            compareLetter = currLine[k]
            #print("Current", currLetter)
            #print("Compare", compareLetter)
            if(compareLetter == currLetter):
                matchCount = matchCount + 1
                #print("Match Count = ", matchCount)
        
        if(matchCount == 2):
            twoFound = 1
            #print("Twos = ", twoCounter)
        if(matchCount == 3):
            threeFound = 1
            #print("Threes = ", threeCounter)
        #print("Clear Match Count")
        matchCount = 0
    if(twoFound):
        twoCounter += 1
    if(threeFound):
        threeCounter += 1
    twoFound = 0
    threeFound = 0
        

twoCounter = twoCounter
threeCounter = threeCounter
#print(twoCounter)
#print(threeCounter)
answer = (twoCounter*threeCounter)

print(answer)
                
            
            
        
