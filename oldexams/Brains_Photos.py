n,m = map(int,raw_input().strip().split())
flag = False
for a in range(n):
    str1 = raw_input().strip()
    if ('C' in str1 or 'Y' in str1 or 'M' in str1) and not flag: 
        print "#Color"
        flag = True
if not flag:
    print "#Black&White"
