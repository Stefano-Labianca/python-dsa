from data_structures.queue import Queue

class Graph:
    def __init__(self):
        self.graph = dict()

    def depth_first_search(self, start_vertex):
        return self.__depth_first_search_r([], start_vertex)

    def __depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighboors = sorted(self.graph[current_vertex])

        for v in neighboors:
            if v not in visited:
                visited = self.__depth_first_search_r(visited, v)

        return visited

    def breadth_first_search(self, v):
        visited = [v]
        queue = Queue()
        queue.push(v)
    
        while not queue.is_empty():
            node = queue.pop()

            if node == None: break

            neighboors = sorted(self.graph[node.val])

            for n in neighboors:
                if n not in visited:
                    visited.append(n)
                    queue.push(n)
                    
        return visited

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