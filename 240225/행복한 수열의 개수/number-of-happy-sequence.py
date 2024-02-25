N, A = map(int, input().split())

if A == 1:
    print(N+N)
    exit()

M = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    M[i] = list(map(int, input().split()))

result = 0

for i in range(N):
    count = 1
    for j in range(N-1):
        if M[i][j] == M[i][j+1]:
            count+=1
            if count >= A:
                result += 1
                break



for i in range(N):
    count = 1
    for j in range(N-1):
        if M[j][i] == M[j+1][i]:
            count+=1
            if count >= A:
                result += 1
                break



print(result)