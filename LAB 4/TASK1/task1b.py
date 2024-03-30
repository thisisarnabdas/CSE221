def adjList(inp):
    vertices, edges = [int(i) for i in inp.readline().split()]
    adjList = [[] for i in range(vertices + 1)]

    for i in range(edges):
        u, v, w = [int(i) for i in inp.readline().split()]
        adjList[u].append((v, w))

    return adjList


inp = open("input1b.txt", "r")
out = open("output1b.txt", "w")
lst = adjList(inp)
for k in range(len(lst)):
    out.write(f"{k}: {" ".join(str(x) for x in lst[k])}")
    out.write("\n")
