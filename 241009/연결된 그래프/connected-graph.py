n, m = map(int, input().split())
dic = dict()

for _ in range(m):
    st, en = map(int, input().split())
    dic.setdefault(st, []).append(en)

nodes = set()
visited = [False for i in range(n+1)]
stk = [dic[1]]
for d in dic[1]:   
    nodes.add(d)

while stk:
    slist = stk.pop()
    for s in slist:
        nslist = dic.get(s, [])
        for ns in nslist:
            if visited[ns]: continue

            visited[ns] = True
            nodes.add(ns)
            stk.append([ns])

print(len(nodes))