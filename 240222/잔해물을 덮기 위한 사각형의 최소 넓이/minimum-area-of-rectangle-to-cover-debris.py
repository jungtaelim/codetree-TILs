MM = 1000

M = [[0 for i in range(2*MM+1)] for j in range(2*MM+1)]

for i in range(2):
    a,b,c,d = map(int, input().split())
    if i == 0:
        for j in range(MM+a,MM+c):
            for k in range(MM+b,MM+d):
                M[j][k] = 1
    else:
        for j in range(MM+a,MM+c):
            for k in range(MM+b,MM+d):
                M[j][k] = 0
Hx = -2*MM+1
Hy = -2*MM+1
Lx = 2*MM+1
Ly = 2*MM+1
flag = False
for i in range(MM*2+1):
    for j in range(MM*2+1):
        if M[i][j] == 1:
            if Hx < i:
                Hx = i
                flag = True
            if Hy < j:
                Hy = j
                flag = True
            if Lx > i:
                Lx = i
                flag = True
            if Ly > j:
                Ly = j
                flag = True

if flag:
    print(abs(Hx+1-Lx)*abs(Hy+1-Ly))
else:
    print(0)