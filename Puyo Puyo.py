from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(x, y):
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < 12 and 0 <= Y < 6:
            if board[X][Y] == board[x][y] and visited[X][Y] == 0:
                q.append([X, Y])
                visited[X][Y] = 1

def gravity():
    for y in range(6):
        bag = deque([])
        for x in range(11, -1, -1):
            if board[x][y] != '.':
                bag.append(board[x][y])
        for x in range(11, -1, -1):
            if bag:
                board[x][y] = bag.popleft()
            else:
                board[x][y] = '.'

board = []
for _ in range(12):
    board.append(list(input()))

chk = 0
answer = 0
while True:
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque([[i, j]])
                st = []
                while q:
                    now = q.popleft()
                    st.append(now)
                    BFS(now[0], now[1])
                if len(st) >= 4:
                    chk = 1
                    for s in st:
                        board[s[0]][s[1]] = '.'
    gravity()
    if chk == 0:
        break
    chk = 0
    answer += 1
print(answer)