# 14:35
# n: 회전 가능 레벨, 주어진 격자의 크기: 2의 n승 * 2의 n승
# q: 회전 횟수
n, q = map(int, input().split())
N = pow(2, n)
board = []
for i in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)


rotateLevels = list(map(int, input().split()))
print("LEVELS", rotateLevels)

def printBoard():
    for i in range(N):
        print(board[i])
### 함수 구현부
def rotate(mapWidth, oneBoardWidth): # 4, 2 => 레벨2
    for i in range(0, N, mapWidth):
        for j in range(0, N, mapWidth):
            print("StartPoint", i, j)
            # 좌하, 우하, 우상, 좌상(저장값불러오기) 순으로 이동
            # 좌상 저장
            leto = [x[j:j+oneBoardWidth] for x in board[i:i+oneBoardWidth]]
            print(leto)
            
            #좌하 > 좌상
            for ni in range(i, i+oneBoardWidth):
                for nj in range(j, j+oneBoardWidth):
                    board[ni][nj] = board[ni+oneBoardWidth][nj]
            
            #우하 > 좌하
            for ni in range(i, i+oneBoardWidth):
                for nj in range(j+oneBoardWidth, j+oneBoardWidth+oneBoardWidth):
                    print("PP",ni, nj)
                    board[ni][nj] = board[ni][nj+oneBoardWidth]


    printBoard()


### 수행부
for level in rotateLevels:
    rotateChoiceWidth = pow(2, level)
    rotateOneBoardWidth = pow(2, level-1)
    print(level, rotateChoiceWidth, rotateOneBoardWidth)
    rotate(rotateChoiceWidth, rotateOneBoardWidth)