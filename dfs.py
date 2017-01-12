from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.costdict = {}

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.costdict[(u, v)] = w

    def DFSutil(self, source, destination, visited):
        visited[destination] = True
        print(destination)
        if source or destination != 0:
            print("cost is" + str(self.costdict[(source, destination)]))
        for v, w in self.graph[destination]:
            if visited[v] == False:
                self.DFSutil(destination, v, visited)

    def DFS(self, v):
        visited = [False]*len(self.graph)
        self.DFSutil(0, v, visited)

g = Graph(3)
g.addEdge(0, 1, 3)
g.addEdge(0, 2, 3)
g.addEdge(1, 2, 3)
g.addEdge(2, 0, 3)
g.addEdge(2, 3, 3)
g.addEdge(3, 3, 3)
g.DFS(0)
