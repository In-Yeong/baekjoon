def DFS(x, y):
    global answer
    if board[x][y] == 1:    # 해당 칸에 1이 적혀있으면
        for k in range(5, 0, -1):           # 5부터 1까지
            if mydict[k] > 0 and x+k <= 10 and y+k <= 10:   # 색종이가 떨어지지 않았고, 해당 색종이를 붙일 범위가 존재하면
                ck = 0
                for i in range(k):                  # 색종이 붙일 영역이 모두 1인지 확인
                    for j in range(k):
                        if board[x + i][y + j] == 0:
                            ck = 1          # 0이 하나라도 있으면 체크
                            break
                    if ck == 1:
                        break

                if ck == 0:         # 붙일 영역이 모두 1이면
                    mydict[k] -= 1      # 색종이 하나 빼서 쓰기
                    for i in range(k):          # 색종이 붙임 (0 처리)
                        for j in range(k):
                            board[x + i][y + j] = 0

                    if y < 9:           # 다음 칸으로 이동 (39~49번 줄과 동일)
                        DFS(x, y + 1)
                    elif x < 9:
                        DFS(x + 1, 0)
                    else:
                        sub = 0
                        for i in range(1, 6):
                            sub += 5 - mydict[i]
                        if sub < answer:
                            answer = sub
                        return

                    mydict[k] += 1              # 재귀 후 색종이 회수
                    for i in range(k):      # 덮었던 색종이 다시 뺌 (1 처리)
                        for j in range(k):
                            board[x + i][y + j] = 1

    else:           # 해당 칸에 0이 적혀 있으면 다음 칸으로 이동
        if y < 9:           # 오른쪽 끝까지 오지 않았으면
            DFS(x, y+1)     # 오른쪽으로 한칸 이동
        elif x < 9:         # 오른쪽 맨 끝에 오고 아직 마지막 줄이 아니면
            DFS(x+1, 0)     # 다음 줄(한칸 아래 맨 왼쪽)로 이동
        else:               # 10열 10행이면
            sub = 0
            for i in range(1, 6):
                sub += 5 - mydict[i]        # 쓴 색종이를 sub에 더함
            if sub < answer:        # 쓴 색종이가 현재보다 적으면 답 갱신
                answer = sub
            return

board = []
mydict = {1:5, 2:5, 3:5, 4:5, 5:5}  # 색종이 개수
answer = 987654321      # 불가능한 값 넣기
for _ in range(10):
    board.append(list(map(int, input().split())))

DFS(0, 0)

if answer == 987654321:     # 한번도 10열 10행에 도달하지 못했다면
    answer = -1         # 불가능 처리

print(answer)