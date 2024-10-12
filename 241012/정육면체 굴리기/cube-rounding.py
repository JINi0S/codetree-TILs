N, M, x, y, k = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

moveList = list(map(int, input().split()))

direction = {
    1:[0,1],
    2:[0,-1],
    3:[-1,0],
    4:[1,0]
}


def inRange(rx, ry):
    return 0 <= rx < N and 0 <= ry < M

dice = [0 for _ in range(7)]


def move(dr):
    global dice
    # 탑 바텀 북 남 동 서
    top, bottom, north, south, east, west = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]

    if dr == 1:  # 동
        (dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]) = (west, east, north, south, top, bottom)
    elif dr == 2: # 서
        (dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]) = (east, west, north, south, bottom, top)
    elif dr == 3: # 북
        (dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]) = (south, north, top, bottom, east, west)
    elif dr == 4:  # 남
        (dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]) = (north, south, bottom, top, east, west)

# 동1, 서2, 북3, 남:4
for moveD in moveList:
    
    nx = x + direction[moveD][0]
    ny = y + direction[moveD][1]
    if not inRange(nx,ny): continue
   
    move(moveD)
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[2]
    else:
        dice[2] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[1])
    x = nx
    y = ny