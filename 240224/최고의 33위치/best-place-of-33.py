N = int(input())

M = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    M[i] = list(map(int, input().split()))

max1 = 0
for i in range(N):
    for j in range(N):
        if i+2<N and j+2<N:
            sum1 = 0
            for k in range(3):
                for w in range(3):
                    sum1 = sum1 + M[i+k][j+w]
            if sum1 > max1:
                max1 = sum1

print(max1)