"""
처음 주사위 이동방향 : 동쪽

[이동 방식]
1. 이동방향으로 한 칸 굴러감.
    - 이동방향에 칸이 없으면 반대로 한 칸 굴러감
2. 도착한 칸에 대한 점수 획득
3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸에 있는 정수B를 비교해 이동방향 결정
    - A > B이면, 이동방향 90도 시계방향 회전
    - A < B이면, 이동방향 90도 반시계방향 회전
    - A = B이면, 이동방향에 변화 없음

[점수 획득 방식]
칸(x,y)에 있는 정수를 B라고 했을 떄,
1. (x,y)에서 동서남북으로 연속해서 이동할 수 있는 칸의 수 C를 구함.
2. B * C (= 두 정수를 곱한 값)
"""


# 전역 변수 선언부
dice = [1, 6, 5, 2, 3, 4]   #  위 아래 북 남 동 서
now_d = 1
x, y = 0, 0  # 주사위 시작 좌표
answer = 0
direction = {
    1: [0, 1],  # 동
    2: [1, 0],  # 남
    3: [0, -1],  # 서
    4: [-1, 0]  # 북
}


def inRange(rx, ry):
    return 0 <= rx < N and 0 <= ry < N


def getScore():
    global x, y

    boardValue = board[x][y]
    stk = [(x, y)]
    cnt = 1
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    while stk:
        sx, sy = stk.pop()

        for i in range(1, 5):
            nnx = sx + direction[i][0]
            nny = sy + direction[i][1]
            if not inRange(nnx, nny): continue
            if visited[nnx][nny]: continue
            if board[nnx][nny] != boardValue: continue

            stk.append((nnx, nny))
            visited[nnx][nny] = True
            cnt += 1
    # print("점수 세기,",cnt, boardValue, "==>" , cnt * boardValue)
    return cnt * boardValue


def moveDice(diceDir):
    # 인덱스에 해당하는 위치 ====>  위 아래 북 남 동 서
    top, bottom, north, south, east, west = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if diceDir == 1:  # 동쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = west, east, north, south, top, bottom
    elif diceDir == 2:  # 남쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = north, south, bottom, top, east, west
    elif diceDir == 3:  # 서쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = east, west, north, south, bottom, top
    elif diceDir == 4:  # 북쪽으로 이동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = south, north, top, bottom, east, west


def changeDir():  # 180회전
    global now_d
    if now_d <= 2:
        now_d += 2
    else:
        now_d -= 2


def nextDir():
    global now_d, x, y
    if dice[1] > board[x][y]:
        now_d += 1
        if now_d >= 5:
            now_d = 1
    elif dice[1] < board[x][y]:
        now_d -= 1
        if now_d <= 0:
            now_d = 4



# 입력부
N, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


# 구현부 ( 반복 이동 )
for _ in range(K):
    # print("반복 시작:===",x, y, "이동방향: ", now_d)
    nx = x + direction[now_d][0]
    ny = y + direction[now_d][1]

    if not inRange(nx, ny):
        changeDir()
        nx = x + direction[now_d][0]
        ny = y + direction[now_d][1]
    # print("다음 좌표와 방향", nx, ny, now_d)
    moveDice(now_d)

    x, y = nx, ny
    answer += getScore()
    nextDir()
    # print("다음 이동방향:", now_d)
print(answer)