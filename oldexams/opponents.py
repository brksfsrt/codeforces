n,d = map(int,raw_input().split())
count = 0
temp = 0
for i in range(d):
    string = str(raw_input())
    number = 0
    for char in string:
        if char == '1':
            number += 1
    if number != n:
        temp += 1
    else:
        temp = 0
    if temp > count:
        count = temp
print count
