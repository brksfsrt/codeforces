temp = raw_input().split()
n = int(temp[0])
m = int(temp[1])
k = 823542
ret = 1

if m > k or n > k:
    print 0

else:
    if m < 7 and n < 7:
        print (m-1)*(n-1)
    else:
        count = 7
        while n > 0:
            if n/7 > 0:
                ret *= count
                count -= 1
                n /= 7
            else:
                ret *= min(count,n%7)
                count -= 1
                n /= 7
        while m/7 > 0:
            if m/7 > 0:
                ret *= count
                count -= 1
                m /= 7
            else:
                ret *= min(count,m%7)
                m /= 7

print ret
