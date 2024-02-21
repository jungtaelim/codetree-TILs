MM = 100

M = [[0 for i in range(MM*2+1)] for j in range(MM*2+1)]


N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    curx = 100 + x
    cury = 100 + y
    for j in range(8):
        for k in range(8):
            M[curx+j][cury+k] = 1

count = 0
for i in range(2*MM+1):
    for j in range(2*MM+1):
        if M[i][j] == 1:
            count += 1

print(count)