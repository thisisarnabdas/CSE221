result = []
visited = set()


def dfs(G, v, visited, track):
    visited.add(v)
    result.append(v)

    for neighbour in G[v]:
        track[neighbour] -= 1

        if neighbour not in visited and track[neighbour] == 0:
            dfs(G, neighbour, visited, track)


inp = open('input1a.txt', 'r')
out = open('output1a.txt', 'w')

n, m = [int(i) for i in inp.readline().split()]

my_dict = {}
for i in range(1, n + 1):
    my_dict[i] = []

track = [0] * (n + 1)
for i in range(m):
    pre_req, course = [int(i) for i in inp.readline().split()]
    my_dict[pre_req].append(course)
    track[course] += 1

for i in range(1, n + 1):
    if track[i] == 0 and i not in visited:
        dfs(my_dict, i, visited, track)

if len(result) < n:
    out.write('IMPOSSIBLE')
else:
    out.write(str(result).strip('[]').replace(',', ''))
