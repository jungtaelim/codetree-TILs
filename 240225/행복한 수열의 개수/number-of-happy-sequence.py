N, A = map(int, input().split())

M = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    M[i] = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(N):
        for k in range(2):
            if j+k+1 <N and M[i][j+k+1] == M[i][j+k]:
                count += 1
            else:
                count = 1
            if count >= A:
                count = 1
                result += 1
                break
        for k in range(3):
            if i+k+1<N and M[i+k][j] == M[i+k+1][j]:
                count += 1
            else:
                count = 1
            if count >= A:
                count = 1
                result += 1
                break
print(result/2)