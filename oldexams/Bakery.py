def binarySearch(alist,item):
    first = 0
    last = len(alist)- 1
    found = False
    while first <= last and not found:
        middle = (first+last)/2
        if alist[middle] == item:
            fount = True
        else:
            if item < alist[middle]:
                last = middle-1
            else:
                first = middle+1
    return found

n,m,k = map(int,raw_input().strip().split())
arr = [[-1 for a in range(n+1)] for a in range(n+1)]
harita = []
for a in range(m):
    x,y,z = map(int,raw_input().strip().split())
    if arr[x][y] != -1 and arr[x][y] > z:
        arr[x][y] = z
    harita.append([x,y,z])
if k:
    arr2 = map(int,raw_input().strip().split())
    arr2.sort()
    temp = sorted(arr,key= lambda second:arr[2])
    minimum= -1
    for a in range(m):
        if ((binarySearch(arr2,harita[a][0])) and not(binarySearch(arr2,harita[a][1]))) or (not(binarySearch(arr2,harita[a][0])) and (binarySearch(arr2,harita[a][1]))):
            if minimum == -1 or minimum > harita[2]:
                minimum = harita[2]
    print minimum
if not k:
    print -1
