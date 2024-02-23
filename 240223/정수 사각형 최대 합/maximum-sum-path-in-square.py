from collections import deque

N = int(input())
M = [[0 for i in range(N)] for j in range(N)]
V = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    M[i] = list(map(int, input().split()))

V[0][0] = M[0][0]
q = deque()
q.appendleft((0, 0))

dir1 = [(1, 0), (0, 1)]

while q:
    x, y = q.popleft()

    for (a, b) in dir1:
        if 0 <= x + a < N and 0 <= y + b < N:
            if V[x + a][y + b] < V[x][y] + M[x + a][y + b]:
                V[x + a][y + b] = V[x][y] + M[x + a][y + b]
                if V[x+a][y+b]!=0:
                    q.appendleft((x + a, y + b))

print(V[N - 1][N - 1])