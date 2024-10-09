# 14:35 ~ 16:45
# n: 회전 가능 레벨, 주어진 격자의 크기: 2의 n승 * 2의 n승
# q: 회전 횟수
n, q = map(int, input().split())
N = pow(2, n)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

board = []
for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)

rotateLevels = list(map(int, input().split()))

def printBoard():
    for i in range(N):
        print(board[i])

### ===== 함수 구현부
def rotate(mapWidth, oneBoardWidth): # 4, 2 => 레벨2
    for i in range(0, N, mapWidth):
        for j in range(0, N, mapWidth):
            # 좌하, 우하, 우상, 좌상(저장값불러오기) 순으로 이동
            # 좌상 저장
            leto = [x[j:j+oneBoardWidth] for x in board[i:i+oneBoardWidth]]
            
            #좌하 > 좌상
            for ni in range(i, i+oneBoardWidth):
                for nj in range(j, j+oneBoardWidth):
                    board[ni][nj] = board[ni+oneBoardWidth][nj]
            
            #우하 > 좌하
            for ni in range(i+oneBoardWidth, i+oneBoardWidth+oneBoardWidth):
                for nj in range(j, j+oneBoardWidth):
                    board[ni][nj] = board[ni][nj+oneBoardWidth]

            #우상 > 우하
            for ni in range(i+oneBoardWidth, i+oneBoardWidth+oneBoardWidth):
                for nj in range(j+oneBoardWidth, j+oneBoardWidth+oneBoardWidth):
                    board[ni][nj] = board[ni-oneBoardWidth][nj]
            
            #백업 > 우상
            for ni in range(i, i+oneBoardWidth):
                for nj in range(j+oneBoardWidth, j+oneBoardWidth+oneBoardWidth):
                    board[ni][nj] = leto[ni%oneBoardWidth][nj%oneBoardWidth]


def inRange(x):
    if 0<=x<N:
        return True
    else:
        return False


def melting():
    global dx, dy, board

    newBoard = [x[:] for x in board]

    for i in range(N):
        for j in range(N):
            if board[i][j] <= 0: continue
            cnt = 0
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                
                if inRange(nx) and inRange(ny) and board[nx][ny] >= 1:
                    cnt += 1
            if cnt < 3:
                newBoard[i][j] -= 1

    board = [x[:] for x in newBoard]
 

def getOutput():
    stk = []
    visited = [[False for _ in range(N)] for i in range(N)]
    maxSize = 0
    sumV = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] <= 0: continue
            if visited[i][j]: continue
            stk.append((i, j))
            visited[i][j] = True
            size = 1
            sumV += board[i][j]
            while stk:
                s = stk.pop()
                for d in range(4):
                    nx, ny = s[0] + dx[d], s[1] + dy[d]
                    if inRange(nx) and inRange(ny) and board[nx][ny] >= 1 and not visited[nx][ny]:
                        size += 1
                        visited[nx][ny] = True
                        sumV += board[nx][ny]
                        stk.append((nx, ny))
            maxSize = max(maxSize, size)

    print(sumV)
    print(maxSize)


### ==== 반복수행부
for level in rotateLevels:
    if level != 0: 
        rotateChoiceWidth = pow(2, level)
        rotateOneBoardWidth = pow(2, level-1)
        rotate(rotateChoiceWidth, rotateOneBoardWidth)
    melting()

getOutput()