# do dfs starting from node n
# visit all of its children
# once one of the children meet an already visited component or it has no children
# which basically after the all loop: insert into stack (like a bread crumbs) so you track the steps and how it walks through the graph
# then transpose the graph and following the stack do a dfs on it
from collections import defaultdict
from collections import deque


def scc():
    graph = defaultdict(list)
    tgraph = defaultdict(list)

    edges = [[0, 1], [1, 2], [2, 3], [2, 4], [
        3, 0], [4, 5], [5, 6], [6, 4], [6, 7]]
    for i in edges:
        graph[i[0]].append(i[1])
    for i in edges:
        tgraph[i[1]].append(i[0])
    visited = set()
    stack = deque()

    def visit(g, v):
        visited.add(v)
        for neighbor in g[v]:
            if neighbor not in visited:
                visit(g, neighbor)
        stack.append(v)
    visit(graph, list(graph.keys())[0])

    def visit_transpose(g, v):
        visited.add(v)
        for neighbor in g[v]:
            if neighbor not in visited:
                visit(g, neighbor)
    visited = set()
    scc = []
    i = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            i += 1
            visit_transpose(tgraph, node)

    return i


print(scc())
