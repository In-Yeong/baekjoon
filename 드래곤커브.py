def go(D):
    dlist.append(D)
    if D == 0:
        now[0] += 1
    elif D == 1:
        now[1] -= 1
    elif D == 2:
        now[0] -= 1
    else:
        now[1] += 1
    board[now[0]][now[1]] = 1

N = int(input())

board = [[0]*1000 for _ in range(1000)]
# 500, 500을 0,0으로 취급

for n in range(N):
    x, y, d, g = map(int, input().split())
    board[500 + x][500 + y] = 1
    now = [500 + x, 500 + y]
    dlist = []
    go(d)
    for i in range(g):
        for j in range(len(dlist)-1, -1, -1):
            go((dlist[j]+1)%4)

answer = 0
for i in range(1000):
    for j in range(1000):
        if board[i][j] == 1:
            if board[i+1][j] == 1 and board[i+1][j+1] == 1 and board[i][j+1] == 1:
                answer += 1

print(answer)