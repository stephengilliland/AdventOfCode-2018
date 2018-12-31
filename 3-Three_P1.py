inputFile = open('2-Input.txt', 'r')

count = len(open('2-Input.txt').readlines(  ))
d = []

currPoint = 0
SN = 3999
currPower = 0
bestPower = 0
locX = 0
locY = 0
x = 0
for y in range(1, 301):
    for x in range(1, 301):
        currPoint = (((x+10)*y)+SN)*(x+10)
        while(currPoint > 999):
            currPoint -= 1000
        while((currPoint % 100) > 0):
            currPoint -= 1
        if(currPoint > 99):
            currPoint //= 100
        else:
            currPoint = 0
        currPoint -= 5
        d.append(currPoint)

print(len(d))
#for Y in range(1, 298):
for x in range(1, 89300):
    currPower = d[x] + d[x+1] + d[x+2] + d[x+300] + d[x+301] + d[x+302] + d[x+600] + d[x+601] + d[x+602]
    if(currPower > bestPower):
        bestPower = currPower
        locX = x%300 + 1
        locY = x // 300 + 1


print(locX)
print(locY)
print(bestPower)



#print(points)
#print(currPoint)





