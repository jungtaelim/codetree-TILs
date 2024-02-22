MM = 100

M = [[0 for i in range(2*MM+1)] for j in range(2*MM+1)]



N = int(input())
color = 1
for i in range(N):
    a, b, c, d = map(int, input().split())

    for j in range(MM+a,MM+c):
        for k in range(MM+b,MM+d):
            M[j][k] = color
    color *= -1

count = 0
for i in range(2*MM+1):
    for j in range(2*MM+1):
        if M[i][j] == -1:
            count += 1

print(count)