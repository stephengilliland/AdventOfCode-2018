inputFile = open('2-Input.txt', 'r')

count = len(open('2-Input.txt').readlines(  ))
lines = ["" for x in range(count)]
currLine = ""
nextLine = ""
currLetter = ''
bads = 0
lines[0] = inputFile.readline().strip()

for x in range(1, count):
    lines[x] = inputFile.readline().strip()
#print(lines)

for x in range(count):
    currLine = lines[x]
    for m in range(count):
        nextLine = lines[m]
        for i in range(26):
            currLetter = currLine[i]
            nextLetter = nextLine[i]
            #print("Current", currLetter)
            #print("NextLet",nextLetter)
            if(currLetter != nextLetter):
                bads +=1
                #print(bads)
        if(bads == 1):
            print(currLine)
            print(nextLine)
        bads = 0
    #print(bads)

