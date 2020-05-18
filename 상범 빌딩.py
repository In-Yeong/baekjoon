from collections import deque
dh = [-1, 1, 0, 0, 0, 0] # 상하좌우앞뒤
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, -1, 1, 0, 0]

def BFS(h, x, y):   # h: 높이, x: 앞뒤, y: 좌우
    global answer
    for d in range(6):
        H = h + dh[d]
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= H < L and 0 <= X < R and 0 <= Y < C:    # 범위 안에 있다면
            if board[H][X][Y] == '.' and visited[H][X][Y] == 0: # 비어있는 칸이고 방문한 적이 없다면
                visited[H][X][Y] = visited[h][x][y] + 1
                q.append([H, X, Y])
            elif board[H][X][Y] == 'E': # 출구 도착
                answer = visited[h][x][y]   # visited 누적 횟수를 담는다

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:    # 0 0 0이 들어오면 멈춤
        break

    board = []
    visited = []
    S = 0   # 시작점
    for l in range(L):
        flat = []   # 한 층만 볼 때
        sub_v = []
        for r in range(R):
            sub = list(input())
            if S == 0:  # 아직 시작점을 못찾았으면
                for c in range(C):
                    if sub[c] == 'S':   # 값이 S이면
                        S = [l, r, c]   # 시작점 설정
                        break
            flat.append(sub)
            sub_v.append([0]*C)
        input()     # 한줄 띄우는(무의미한) 인풋 처리
        board.append(flat)
        visited.append(sub_v)
    q = deque([])   # BFS를 위해 큐 생성
    q.append(S)     # 시작점 추가
    visited[S[0]][S[1]][S[2]] = 1   # 시작점 방문 기록
    answer = 0
    while q:    # 방문할 지점이 남아있는 동안
        target = q.popleft()    # 큐에서 방문 지점을 꺼내서
        BFS(target[0], target[1], target[2])    # BFS 돌림
        if answer != 0:     # 출구를 찾아서 answer가 바뀌었다면
            break   # while문 종료
    if answer == 0:     # 출구를 못찾았다면
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'.format(answer))
