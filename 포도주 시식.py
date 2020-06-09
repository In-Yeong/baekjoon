N = int(input())
wine = [0]
maxi = [0]*(N+1)
for i in range(1, N+1):
    wine.append(int(input()))
    if i < 3:
        maxi[i] = sum(wine)
    else:
        target = []
        target.append(maxi[i-3]+wine[i-1]+wine[i])
        target.append(maxi[i-2]+wine[i])
        target.append(maxi[i-1])
        maxi[i] = max(target)
print(maxi[-1])