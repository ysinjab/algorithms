# Best, Average, Worst: O(V3)
# allPairsShortestPath (G)
#     foreach u in V do
#         foreach v in V do
#             dist[u][v] = ∞
#             pred[u][v] = -1
#         dist[u][u] = 0
#     foreach neighbor v of u do
#         dist[u][v] = weight of edge (u,v)
#         pred[u][v] = u
#     foreach k in V do
#         foreach u in V do
#             foreach v in V do
#                 newLen = dist[u][k] + dist[k][v]
#                 if newLen < dist[u][v] then
#                     dist[u][v] = newLen
#                     pred[u][v] = pred[k][v]
#     end

# this implementation is used to solve a problem in leetcode but the psedu-code above is for find the all shortest paths code
from collections import defaultdict
from itertools import permutations

g =  defaultdict(dict)


equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

for i in range(len(equations)):
    g[equations[i][0]][equations[i][0]] = g[equations[i][1]][equations[i][1]]  = 1.0
    g[equations[i][0]][equations[i][1]] = values[i]
    g[equations[i][1]][equations[i][0]] = 1 / values[i]

for k, i, j in permutations(g, 3):
    if k in g[i] and k in g[j]:
        g[i][j] = g[i][k] * g[k][j]
result = []
for q in queries:
    if q[0] not in g or q[1] not in g:
        result.append(-1.0)
    else:
        result.append(g[q[0]][q[1]])
