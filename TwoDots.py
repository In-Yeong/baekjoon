dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def DFS(x, y):
    global answer
    visited[x][y] = 1
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < N and 0 <= Y < M:
            if board[X][Y] == board[x][y]:
                if visited[X][Y] == 0:
                    my_snake.append([X, Y])
                    DFS(X, Y)
                    my_snake.pop()
                else:
                    if X == my_snake[-2][0] and Y == my_snake[-2][1]:
                        pass
                    else:
                        answer = 'Yes'
                        return
        if answer == 'Yes':
            return

N, M = map(int, input().split())
board = []
visited = [[0]*M for _ in range(N)]
for _ in range(N):
    board.append(input())

answer = 'No'
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            my_snake = [[i, j]]
            DFS(i, j)
        if answer == 'Yes':
            break
    if answer == 'Yes':
        break

print(answer)