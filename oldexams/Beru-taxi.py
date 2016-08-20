x,y = map(int,raw_input().strip().split(" "))
n = (int)(raw_input().strip())
minTime = 9999999.0
import math
for a in range(0,n):
    xi,yi,vi = map(int,raw_input().strip().split(" "))
    temp = (float)(math.sqrt((xi-x)**2+(yi-y)**2)/(float)(vi))
    if temp < minTime:
        minTime = temp
print temp
