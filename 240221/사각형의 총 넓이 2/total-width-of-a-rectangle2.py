MM = 100
N = int(input())
M = [[0 for i in range(2*MM+1)] for j in range(2*MM+1)]

for i in range(N):
    a,b,c,d = map(int, input().split())

    for j in range(a,c):
        for k in range(b,d):
            M[j][k] = 1

count = 0
for i in range(2*MM+1):
    for j in range(2*MM+1):
        if M[i][j] == 1:
            count += 1

print(count)