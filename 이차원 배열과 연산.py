def func(B, ga, se):    # 가로로 한 줄씩 연산 실행하고 결과 반환
    newlist = [[] for _ in range(ga)]   # 저장할 리스트
    maxi = 0    # 세로 최대값을 갱신
    for i in range(ga):
        mydict = dict()     # 라인 별 숫자를 세기 위한 딕셔너리
        for j in range(se):
            if B[i][j] != 0:    # 0은 무시한다
                if B[i][j] in mydict:   # 값이 있을 경우 +1 한다
                    mydict[B[i][j]] += 1
                else:   # 값이 없을 경우 1을 배치한다
                    mydict[B[i][j]] = 1
        mylist = list(mydict.items())   # (key, value) 저장
        mylist.sort(key=lambda x: (x[1], x[0])) # value 오름차순으로 정렬 후 value가 같다면 key 오름차순으로 정렬
        newlist[i] = [item for l in mylist for item in list(l)]     # 튜플을 제거한다
        if len(newlist[i]) > 100:   # 100개가 넘어가면 100개까지만 자른다
            newlist[i] = newlist[i][:100]
        if len(newlist[i]) > maxi:  # maxi 갱신
            maxi = len(newlist[i])
    for i in range(ga):     # maxi 길이에 미치지 못하는 리스트는 그 차만큼 0을 추가한다
        cha = maxi - len(newlist[i])
        if cha > 0:
            newlist[i] += [0] * cha
    se = maxi   # 세로값을 maxi로 갱신
    return (newlist, ga, se)

def switch(B, se): # 2차원 배열을 90도로 돌려주는 함수 (가로, 세로 바뀜)
    B = list(zip(*B))   # B(board)를 하나씩 풀어(*) zip 연산(같은 인덱스 번호끼리 묶어줌)한다
    for i in range(se):
        B[i] = list(B[i]) # zip의 결과는 튜플 형태이므로 리스트로 바꿔준다
    return B

r, c, k = map(int, input().split())
board = []
for _ in range(3):
    board.append(list(map(int, input().split())))
garo = 3    # 초기값
sero = 3
cnt = 0
while True:
    if 0 <= r-1 < garo and 0 <= c-1 < sero and board[r-1][c-1] == k:    # 타겟이(r,c) 목표(k)를 만족하면 break
        break

    if cnt >= 100:  # 100번 넘게 돌아가면 -1(실패)로 바꾸고 break
        cnt = -1
        break

    if garo >= sero:    # 가로 연산(R 연산)을 할 경우
        board, garo, sero = func(board, garo, sero) # 바로 연산 실행
    else:   # 세로 연산(C 연산)을 할 경우
        board = switch(board, sero) # 가로 연산을 사용하기 위해 90도 돌린다
        board, sero, garo = func(board, sero, garo) # 가로 연산 실행
        board = switch(board, garo) # 결과를 다시 90도 돌려 세로 연산을 한 것처럼 만든다
    cnt += 1    # 카운트
print(cnt)