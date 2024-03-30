import numpy as np


def adjMat(inp):
    vertices, edges = [int(i) for i in inp.readline().split()]
    relation = []
    for i in range(edges):
        relation.append([int(i) for i in inp.readline().split()])
    adjMat = np.zeros((vertices + 1, vertices + 1), dtype=int)  # Creates NxN matrix
    for j in range(len(relation)):
        u, v, weight = relation[j]
        adjMat[u][v] = weight
    return np.array(adjMat)


inp = open("input1a.txt", "r")
out = open("output1a.txt", "w")
matrices = adjMat(inp)
out.write(str(matrices).replace(' [', '').replace('[', '').replace(']', ''))
