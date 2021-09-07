class Graph:
    def __init__(self,adj={}):
        self.adj = adj
        self.nodes = []
        self.nodes = list(adj)
        for n in self.adj:
            self.nodes += list(self.adj[n])
        self.nodes = list(set(self.nodes))

        for n in self.nodes:
            if n not in self.adj:
                self.adj[n] = {}
