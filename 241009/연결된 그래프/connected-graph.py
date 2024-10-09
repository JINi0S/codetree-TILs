n, m = map(int, input().split())
dic = dict()

for _ in range(m):
    st, en = map(int, input().split())
    dic.setdefault(st, set()).add(en)
    dic.setdefault(en, set()).add(st)

nodes = set()
visited = [False for i in range(n+1)]
stk = [1]

for d in dic.get(1, []):   
    nodes.add(d)

while stk:
    current= stk.pop()
    for s in dic.get(current, []):
        if visited[s] and s != 1: continue
        visited[s] = True
        nodes.add(s)
        stk.append(s)

nodes.discard(1)
print(len(nodes))

# visited = [False for _ in range(n+1)]
# stk = [1]  # 시작 노드 1을 스택에 넣음
# visited[1] = True  # 시작 노드 1은 방문 처리
# nodes = set()

# while stk:
#     current = stk.pop()  # 현재 노드 탐색
#     for neighbor in dic.get(current, []):  # 인접 노드 탐색
#         if not visited[neighbor]:  # 방문하지 않은 노드만
#             visited[neighbor] = True  # 방문 처리
#             nodes.add(neighbor)  # 노드 집합에 추가
#             stk.append(neighbor)  # 스택에 추가

# print(len(nodes))