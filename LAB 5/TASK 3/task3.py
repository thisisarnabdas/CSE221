stack = []
visited = set()


def dfs(G, v, visited, Top_sort=True, StrongL=None):
    visited.add(v)
    if not Top_sort:
        StrongL.append(v)

    for neighbour in G[v]:
        if neighbour not in visited:
            dfs(G, neighbour, visited, Top_sort, StrongL)

    if Top_sort:
        stack.append(v)


inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

n, m = [int(i) for i in inp.readline().split()]

graph = {}
reverseG = {}
for i in range(n + 1):
    graph[i] = []
    reverseG[i] = []

for i in range(m):
    u, v = [int(i) for i in inp.readline().split()]
    graph[u].append(v)
    reverseG[v].append(u)

for i in range(1, n + 1):
    if i not in visited:
        dfs(graph, i, visited)

visited.clear()
scc = []
while stack:
    lst = []
    node = stack.pop()
    if node not in visited:
        dfs(reverseG, node, visited, Top_sort=False, StrongL=lst)

    if lst:
        scc.append(lst)
print(scc)
for i in scc:
    for j in i:
        out.write(str(j) + " ")
    out.write("\n")
