n,m = map(int,raw_input().split())
arr = [0]*(n+1)
flag = False
for road in range(m):
    v1,v2 = map(int,raw_input().split())
    if arr[v1] == 0 and arr[v2] == 0:
        arr[v1] = 1
        arr[v2] = -1
    elif arr[v1] <= -1 and arr[v2] > -1:
        arr[v2] += 1
        arr[v1] += -1
    elif arr[v1] >= 1 and arr[v2] < 1:
        arr[v2] += -1
        arr[v1] += 1
    elif arr[v2] <= -1 and arr[v1] > -1:
        arr[v1] += 1
        arr[v2] += -1
    elif arr[v2] >= 1 and arr[v1] < 1:
        arr[v1] += -1
        arr[v2] += 1
    else:
        flag = True
    if (arr[v1] > 0 and arr[v2]  > 0) or (arr[v1] < 0 and arr[v2] < 0):
        flag = True
if not flag:
    total1 = 0
    total2 = 0
    for index in range(1,n+1):
        if arr[index] < 0:
            total2 += abs(arr[index])
        else:
            total1 += abs(arr[index])
    if total1 != total2:
        print -1
    else:
        print len(filter(lambda x: x< 0, arr))
        for index,number in enumerate(arr):
            if number < 0:
                print index,
        print
        print len(filter(lambda x: x>0,arr))
        for index,number in enumerate(arr):
            if number > 0:
                print index,
if flag:
    print -1
