from copy import deepcopy
from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    board[x][y] = cnt
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < sero and 0 <= Y < garo:
            if board[X][Y] == 1:
                DFS(X, Y)

def bridge(x, y):
    start = board[x][y]
    for d in range(4):
        end = 0
        X = x
        Y = y
        ck = 0
        while True:
            X += dx[d]
            Y += dy[d]
            if 0 <= X < sero and 0 <= Y < garo:
                if board[X][Y] == 0:
                    ck += 1
                else:
                    end = board[X][Y]
                    break
            else:
                break
        if start == end:
            continue
        if ck > 1:
            if end != 0:
                if B[start][end] == 'x':
                    B[start][end] = ck
                    B[end][start] = ck
                    line_list.append([start, end])
                else:
                    if ck < B[start][end]:
                        B[start][end] = ck
                        B[end][start] = ck

def final_sub(x, sub, b):
    b.append(x)
    for f in range(2, cnt):
        if sub[x][f] == 1 and f not in b:
            final_sub(f, sub, b)

def final(Llist):
    test = [[0]*cnt for _ in range(cnt)]
    for l in Llist:
        test[l[0]][l[1]] = 1
        test[l[1]][l[0]] = 1
    box = []
    final_sub(2, test, box)
    if len(box) != cnt-2:
        return False
    else:
        return True

sero, garo = map(int, input().split())
board = []
for i in range(sero):
    board.append(list(map(int, input().split())))

cnt = 2
for i in range(sero):
    for j in range(garo):
        if board[i][j] == 1:
            DFS(i, j)
            cnt += 1

B = [['x']*cnt for _ in range(cnt)]
line_list = deque([])

for i in range(sero):
    for j in range(garo):
        if board[i][j] != 0:
            bridge(i, j)


visited = [[0]*cnt for _ in range(cnt)]
ck = [0]*cnt
answer = 987654321

for i in combinations(line_list, cnt-3):
    if final(i) == True:
        sub_answer = 0
        for j in i:
            sub_answer += B[j[0]][j[1]]
        if sub_answer < answer:
            answer = sub_answer

if answer == 987654321:
    answer = -1

print(answer)
