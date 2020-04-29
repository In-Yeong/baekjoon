dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def spread(x, y):
    cnt = board[x][y]
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < R and 0 <= Y < C:
            if board[X][Y] >= 0:
                sub_board[X][Y] += board[x][y]//5
                cnt -= board[x][y]//5
    sub_board[x][y] += cnt

def cleanup(x):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    now = sub_board[x][1]
    sub_board[x][1] = 0
    d = 0
    X = x
    Y = 1
    while True:
        X += dx[d]
        Y += dy[d]
        next = sub_board[X][Y]
        sub_board[X][Y] = now
        now = next
        if X + dx[d] < 0 or X + dx[d] > x or Y + dy[d] < 0 or Y + dy[d] >= C:
            d += 1
        if d == 4:
            break

def cleandown(x):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    now = sub_board[x][1]
    sub_board[x][1] = 0
    d = 0
    X = x
    Y = 1
    while True:
        X += dx[d]
        Y += dy[d]
        next = sub_board[X][Y]
        sub_board[X][Y] = now
        now = next
        if X + dx[d] < x or X + dx[d] >= R or Y + dy[d] < 0 or Y + dy[d] >= C:
            d += 1
        if d == 4:
            break

R, C, T = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

v1 = 0
v2 = 1
for i in range(R):
    if board[i][0] == -1:
        v1 = i
        v2 = i+1
        break

for _ in range(T):  # 몇회 반복
    sub_board = [[0]*C for __ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                spread(i, j)

    cleanup(v1)
    cleandown(v2)

    sub_board[v1][0] = -1
    sub_board[v2][0] = -1
    board = sub_board

answer = 0
for i in range(R):
    for j in range(C):
        answer += board[i][j]
print(answer+2)

