temp = raw_input().split()
n = int(temp[0])
x = int(temp[1])

distress = 0
remain = x
for a in range(n):
    queue = raw_input().split()
    if queue[0] == '-':
        if int(queue[1]) > remain:
            distress += 1
        else:
            remain -= int(queue[1])
    else:
        remain += int(queue[1])

print remain, distress
