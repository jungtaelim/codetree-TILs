n, m = map(int, input().split())
M = [[0 for i in range(n)] for j in range(n)]


def count_gold(row, col, k):
    return(sum(
        M[i][j]
        for i in range(n)
        for j in range(n)
        if M[i][j] == 1 and abs(row-i) + abs(col-j) <= k
    ))

for i in range(n):
    M[i] = list(map(int, input().split()))

max1 = 0
for k in range(1, n + 1):
    for row in range(n):
        for col in range(n):
            if count_gold(row, col, k) * m - (k * k + (k + 1) * (k + 1)) > 0:
                if max1 < count_gold(row, col, k):
                    max1 = count_gold(row, col, k)
print(max1)