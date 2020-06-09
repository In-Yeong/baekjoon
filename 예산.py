n = int(input())
city = list(map(int, input().split()))
B = int(input())
divi = B//n
extra = 0
over = []
for c in city:
    if divi-c >= 0:
        extra += divi-c
    else:
        over.append(c)
over.sort(reverse=True)
if len(over):
    divi += int(extra//len(over))
    while True:
        if len(over) == 0:
            break
        sumi = 0
        for i in city:
            sumi += min(divi, i)
        if B - sumi >= len(over):
            divi += 1
            while True:
                if len(over) and over[-1] <= divi:
                    over.pop()
                else:
                    break
        else:
            break
else:
    divi = max(city)

print(divi)