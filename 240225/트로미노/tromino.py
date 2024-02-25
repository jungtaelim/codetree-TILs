R,C = map(int, input().split())

M = [[0 for i in range(C)] for j in range(R)]

for i in range(R):
        M[i] = list(map(int, input().split()))


max1 = 0
for i in range(R):
    for j in range(C):
        if i+1<R and j+1<C:
            sum1 = 0
            sum1 = sum1 + M[i][j]+ M[i+1][j]+ M[i][j+1]+M[i+1][j+1] - min(M[i][j], M[i+1][j], M[i][j+1], M[i+1][j+1])
            max1 = max(max1, sum1)

        if i+2<R:
            sum1 = 0
            max1 = max(max1, M[i][j] + M[i+1][j] + M[i+2][j])
        
        if j+2<C:
            sum1 = 0
            max1 = max(max1, M[i][j] + M[i][j+1] + M[i][j+2])



print(max1)