def b_search(target, mylist):
    mini = 0
    maxi = N//2+1
    while True:
        mid = (mini+maxi)//2
        if mylist[mid] < target:
            mini = mid
        else:
            maxi = mid
        if abs(mini-maxi) <= 1:
            mid = mini
            break
    return mid

N, H = map(int, input().split())
s = [0]
j = [0]
for i in range(1, N+1):
    num = int(input())
    if i%2: # 홀수 == 석순
        s.append(num)
    else: # 짝수 == 종유석
        j.append(H-num)

s.sort()
j.sort()
s.append(H+1)
j.append(H+1)

answer = N
cnt = 1

for i in range(1, H+1):
    s_num = b_search(i, s)
    j_num = b_search(i, j)
    result_s = N//2-s_num
    result_j = j_num
    result = result_s+result_j
    if result < answer:
        answer = result
        cnt = 1
    elif result == answer:
        cnt += 1

print(answer, cnt)