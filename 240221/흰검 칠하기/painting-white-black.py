from collections import deque

N = int(input())

M = [[0 for i in range(200001)] for j in range(2)]

x = 100000

for i in range(N):
    a, b = input().split()
    a = int(a)
    for j in range(a):
        if b == 'R':
            M[0][x] = 1
            M[1][x] += 1
            x = x + 1
            

        elif b == 'L':
            M[0][x] = -1
            M[1][x] += 1
            x = x - 1
    if b == 'R':
        x = x - 1
    elif b == 'L':
        x = x + 1    
B = 0
W = 0
G = 0
for i in range(200001):
    if M[1][i] > 3:
        G += 1
    elif M[0][i] == 1:
        B += 1
    elif M[0][i] == -1:
        W += 1

print(W, B, G)