N = int(input())

count = 0
max1 = 1
for i in range(N):
    cur = int(input())
    if i == 0:
        count += 1
    
    elif be < cur:
        count += 1
        if max1 < count:
            max1 = count

    else:
        count = 1

    be = cur
    
print(max1)