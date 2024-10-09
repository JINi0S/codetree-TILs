n, m = map(int, input().split())
dic = dict()

# 그래프 입력
for _ in range(m):
    st, en = map(int, input().split())
    dic.setdefault(st, set()).add(en)
    dic.setdefault(en, set()).add(st)

visited = [False for _ in range(n+1)]
stk = [1]  # 시작 노드 1을 스택에 넣음
visited[1] = True  # 시작 노드 1은 방문 처리
nodes = set()

while stk:
    current = stk.pop()  # 현재 노드 탐색
    for neighbor in dic.get(current, []):  # 인접 노드 탐색
        if not visited[neighbor]:  # 방문하지 않은 노드만
            visited[neighbor] = True  # 방문 처리
            nodes.add(neighbor)  # 노드 집합에 추가
            stk.append(neighbor)  # 스택에 추가

print(len(nodes))