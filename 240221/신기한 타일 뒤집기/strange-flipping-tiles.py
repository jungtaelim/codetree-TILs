MM = 100000


M = [0] * (MM*2+1)

cur = MM

n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'R':
        while a > 0:
            M[cur] = 1
            a -= 1
            if a:
                cur += 1
                


    elif b == 'L':
        while a > 0:
            M[cur] = -1
            a -= 1
            if a:
                cur -= 1

B = 0
W = 0           
for i in range(MM*2+1):
    if M[i] == 1:
        B += 1
    elif M[i] == -1:
        W += 1
print(W, B)