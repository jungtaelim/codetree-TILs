MM = 1000

M = [[0 for i in range(MM*2 + 1)]for j in range(MM*2+1)]

for i in range(3):
    a,b,c,d = map(int, input().split())
    if i == 2:
        for j in range(a,c):
            for k in range(b,d):
                M[j][k] = 0
    else:
        for j in range(a,c):
            for k in range(b,d):
                M[j][k] = 1

count = 0
for j in range(MM*2+1):
            for k in range(MM*2+1):
                if M[j][k] == 1:
                    count += 1

print(count)