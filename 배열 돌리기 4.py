import itertools
from collections import deque
from copy import deepcopy

dx = [0, 1, 0, -1, 0] # 우하좌상빈
dy = [1, 0, -1, 0, 0]

def Rolling(st_X, ed_X, st_Y, ed_Y):
    rolling_list = deque([])
    X = st_X
    Y = st_Y
    for d in range(4):
        while True:
            if st_X <= X <= ed_X and st_Y <= Y <= ed_Y:
                rolling_list.append(sub_board[X][Y])
                X += dx[d]
                Y += dy[d]
            else:
                X -= dx[d]
                Y -= dy[d]
                X += dx[d+1]
                Y += dy[d+1]
                break
    rolling_list.pop()
    ls = rolling_list.pop()
    rolling_list.appendleft(ls)
    for d in range(4):
        while True:
            if st_X <= X <= ed_X and st_Y <= Y <= ed_Y:
                if len(rolling_list) != 0:
                    now = rolling_list.popleft()
                    sub_board[X][Y] = now
                else:
                    break
                X += dx[d]
                Y += dy[d]
            else:
                X -= dx[d]
                Y -= dy[d]
                X += dx[d+1]
                Y += dy[d+1]
                break

N, M, K = map(int, input().split())
board = [[0]*M]
r_list = []
for _ in range(N):
    board.append([0]+list(map(int, input().split())))
for _ in range(K):
    r_list.append(list(map(int, input().split())))

answer = 987654321
for mylist in itertools.permutations(r_list):
    sub_board = deepcopy(board)
    for r in mylist:
        for i in range(r[2]):
            stX = r[0] - r[2] + i
            edX = r[0] + r[2] - i
            stY = r[1] - r[2] + i
            edY = r[1] + r[2] - i
            Rolling(stX, edX, stY, edY)

    for i in sub_board:
        target = sum(i)
        if target != 0 and target < answer:
            answer = target

print(answer)

