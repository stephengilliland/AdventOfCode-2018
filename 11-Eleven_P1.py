currPower, bestPower, locX, locY, currPoint, d = 0, 0, 0, 0, 0, []
for y in range(1, 301):
    for x in range(1, 301):
        currPoint = (((((x+10)*y)+3999)*(x+10)//100)%10) - 5
        d.append(currPoint)
#for Y in range(1, 298):
for x in range(1, 89398):
    currPower = d[x] + d[x+1] + d[x+2] + d[x+300] + d[x+301] + d[x+302] + d[x+600] + d[x+601] + d[x+602]
    if(currPower > bestPower):
        bestPower = currPower
        locX = x%300 + 1
        locY = x // 300 + 1
print('[', locX, ',', locY, ']')






