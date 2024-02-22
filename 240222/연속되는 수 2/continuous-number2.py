N = int(input())
max1 = 0
be = -1
count = 0
for i in range(N):
    cur = int(input())
    if i == 0:
        be = cur
        count += 1
        max1 = 1
        continue

    if be == cur:
        count += 1
        be = cur
        continue

    else:
        if count > max1:
            max1 = count
            count = 1
            be = cur
            continue

print(max1)