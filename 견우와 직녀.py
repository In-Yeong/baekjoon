dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_cross(x, y):  # 교차로면 T, 아니면 F
    garo = 0
    sero = 0
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < N and 0 <= Y < N and board[X][Y] != 1:
            if d < 2:
                sero += 1
            else:
                garo += 1
    if sero != 0 and garo != 0:
        return True
    else:
        return False


def DFS(x, y, ck, status):  # ck: 다리를 만든적이 있으면 1 없으면 0, status: 현재위치가 다리이면 1, 땅이면 0
    global answer
    if x == N - 1 and y == N - 1:
        if visited[x][y] < answer:
            answer = visited[x][y]
        return
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < N and 0 <= Y < N and visited[X][Y] == -1:
            if board[X][Y] == 1:
                visited[X][Y] = visited[x][y] + 1
                if visited[X][Y]+ck*1000 not in memo[X][Y]:
                    memo[X][Y].append(visited[X][Y]+ck*1000)
                    DFS(X, Y, ck, 0)
                visited[X][Y] = -1
            elif board[X][Y] == 0:
                if ck == 0 and is_cross(X, Y) is False and status == 0:
                    n = 1
                    while True:
                        if visited[x][y] < M * n:
                            break
                        else:
                            n += 1
                    visited[X][Y] = M * n
                    if visited[X][Y]+ck*1000 not in memo[X][Y]:
                        memo[X][Y].append(visited[X][Y]+ck*1000)
                        DFS(X, Y, 1, 1)
                    visited[X][Y] = -1
                else:
                    pass
            else:
                if status == 0:
                    n = 1
                    while True:
                        if visited[x][y] < board[X][Y] * n:
                            break
                        else:
                            n += 1
                    visited[X][Y] = board[X][Y] * n
                    if visited[X][Y]+ck*1000 not in memo[X][Y]:
                        memo[X][Y].append(visited[X][Y]+ck*1000)
                        DFS(X, Y, ck, 1)
                    visited[X][Y] = -1
                else:
                    pass


N, M = map(int, input().split())
board = []
memo = [[[-1] for __ in range(N)] for _ in range(N)]    # 이동시간 + ck*1000 (다리를 한번 건넌 경우와 건너지 않은 경우를 나누기 위함)
visited = [[-1] * N for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = 987654321
visited[0][0] = 0
memo[0][0].append(0)
DFS(0, 0, 0, 0)

print(answer)