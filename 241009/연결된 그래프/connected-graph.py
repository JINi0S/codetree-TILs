n, m = map(int, input().split())
dic = dict()

for _ in range(m):
    st, en = map(int, input().split())
    dic.setdefault(st, set()).add(en)
    dic.setdefault(en, set()).add(st)

nodes = set()
visited = [False for i in range(n+1)]
stk = [1]
visited[1] = True

# for d in dic.get(1, []):   
#     nodes.add(d)

while stk:
    current= stk.pop()
    for s in dic.get(current, []):
        if visited[s]: continue
        visited[s] = True
        nodes.add(s)
        stk.append(s)

# nodes.discard(1)
print(len(nodes))