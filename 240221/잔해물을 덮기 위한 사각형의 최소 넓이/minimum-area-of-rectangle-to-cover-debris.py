MM = 1000

M = [[0 for i in range(2*MM+1)] for j in range(2*MM+1)]

for i in range(2):
    a,b,c,d = map(int, input().split())
    if i == 0:
        for j in range(MM+a,MM+c+1):
            for k in range(MM+b,MM+d+1):
                M[j][k] = 1
    else:
        for j in range(MM+a,MM+c+1):
            for k in range(MM+b,MM+d+1):
                M[j][k] = 0
Hx = -2*MM+1
Hy = -2*MM+1
Lx = 2*MM+1
Ly = 2*MM+1

for i in range(MM*2+1):
    for j in range(MM*2+1):
        if M[i][j] == 1:
            if Hx < i:
                Hx = i
            if Hy < j:
                Hy = j
            if Lx > i:
                Lx = i
            if Ly > j:
                Ly = j


print(abs(Hx-Lx)*abs(Hy-Ly))