n, t = map(int, input().split())

M = [0]*n

M = list(map(int, input().split()))

count = 0
max1 = 0
for i in range(n):
    if M[i]>t:
        count+=1
        if max1<count:
            max1 = count
    else:
        count = 0

print(max1)