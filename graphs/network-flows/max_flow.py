
import collections
 
class Graph(dict):
    def __init__(self, V=[], E=[]):
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)
        
    def add_vertex(self, v):
        self[v] = dict()

    def add_edge(self, e):
        u, v, c = e
        self[u][v] = c
        self[v][u] = 0


    def bfs(self, s, t, parent):
        '''Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store that path '''
        print(f'###### BFS is gonna start ######')
        visited = [False] * len(self)
        queue = collections.deque()
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v, rc in self[u].items(): # rc stands for residual capacity 
                if (visited[v] == False) and (rc > 0):
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
 
        # return true if the sink is visited which means there is a path
        if visited[t]:
            print('Congrats 🎉 ! sink is got visited')
        else:
            print('no augmentation path is found and no more flow can be sent 😔')
        return visited[t]

    def edmonds_karp(self, source, sink):
        parent = [-1] * len(self)
        max_flow = 0 

        while self.bfs(source, sink, parent):
            print(f'Here is augmented path details:\nPath edges :')
            path_flow = float("Inf")
            s = sink
            p = []
            while s != source:
                p.append((parent[s], s))
                path_flow = min(path_flow, self[parent[s]][s]) 
                s = parent[s]
            pe = ''
            for i, e in enumerate(reversed(p)):
                pe += f'({e[0]}, {e[1]}, {self[e[0]][e[1]]})'
                if i != len(p) - 1:
                    pe += '➡️'
            print(pe)
            
            max_flow += path_flow
            print(f'path_flow is: {path_flow} and current max flow now is: {max_flow}')
            v = sink
            while v !=  source:
                u = parent[v]
                self[u][v] -= path_flow # flow will be subtracted from the capacity
                self[v][u] += path_flow # and will be added to the reversed edge
                v = parent[v]
            
        return max_flow

V = range(0, 6)
# edge is (from, to, capacity)
E = [(0, 1, 8), (0, 4, 3), (1, 2, 9), (4, 2, 7), (2, 4, 7), (4, 3, 4), (2, 5, 2), (3, 5, 5)] 
g = Graph(V, E)
s = 0
t = 5
print(f'Max Flow: {g.edmonds_karp(s, t)}') # 6
print('\n\n')

E = [(0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12), (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]
g = Graph(V, E)
s = 0
t = 5
print(f'Max Flow: {g.edmonds_karp(s, t)}') # 23
