sumV = 0
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0, i+1):
        sumV += row[j]
print(sumV)