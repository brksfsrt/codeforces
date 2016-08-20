def binarySearch(arr,first,last,key):
    middle = (int)((last+first)/2)
    if first > last:
        return 0
    if key < arr[first]:
        return 0
    if key > arr[last]:
        return last+1
    if arr[middle] > key:
        return binarySearch(arr,first,middle-1,key)
    if arr[middle] <= key:
        return middle-first+1+binarySearch(arr,middle+1,last,key)

n = (int)(raw_input().strip())
arr = map(int,raw_input().strip().split())
m = (int)(raw_input().strip())
arr.sort()
arr2 = []
for a in range(0,m):
    arr2.append((int)(raw_input().strip()))
for a in range(0,m):
    print binarySearch(arr,0,n-1,arr2[a])
