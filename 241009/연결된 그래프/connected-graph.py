n, m = map(int, input().split())
dic = dict()

for _ in range(m):
    st, en = map(int, input().split())
    dic.setdefault(st, []).append(en)
    # dic.setdefault(en, []).append(st)

nodes = set()
visited = [False for i in range(n+1)]
stk = [dic.get(1, [])]
print(stk)
for d in dic.get(1, []):   
    nodes.add(d)

while stk:
    slist = stk.pop()
    for s in slist:
        nslist = dic.get(s, [])
        for ns in nslist:
            if visited[ns] and ns != 1: continue

            visited[ns] = True
            nodes.add(ns)
            stk.append([ns])

nodes.discard(1)
print(len(nodes))