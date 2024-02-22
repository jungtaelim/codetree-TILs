N = int(input())

be = 0
count = 0 
max1 = 1

for i in range(N):
    cur = int(input())
    if i == 0:
        count = 1
    
    elif be * cur > 0:
        count += 1
        if max1 < count:
            max1 = count
    else:
        count = 1
        
    be = cur

print(max1)