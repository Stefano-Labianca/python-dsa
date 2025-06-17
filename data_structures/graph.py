class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        
        if v not in self.graph:
            self.graph[v] = set()

        self.graph[u].add(v)
        self.graph[v].add(u)

    def adjacent_nodes(self, node):
        adj = self.graph[node]
        keys = self.graph.keys()
        
        for key in keys:
            if node == key:
                continue
            
            if node in self.graph[key]:
                adj.add(key)

        return adj
    
    def unconnected_vertices(self):
        keys = self.graph.keys()
        unconnected = []

        for k in keys:
            if len(self.graph[k]) > 0:
                continue

            unconnected.append(k)

        return unconnected

        
    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result