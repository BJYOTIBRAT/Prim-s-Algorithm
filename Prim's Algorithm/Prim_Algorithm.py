import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def prim(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

def print_mst(parent, graph):
    print("Edge   Weight")
    for i in range(1, len(parent)):
        print(parent[i], "-", i, "  ", graph[i][parent[i]])

def main():
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 3)
    g.add_edge(1, 2, 4)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, 6)

    print("Minimal Spanning Tree using Prim's Algorithm:")
    parent = g.prim()
    print_mst(parent, g.graph)

if __name__ == "__main__":
    main()