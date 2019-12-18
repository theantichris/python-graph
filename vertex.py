class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __repr__(self):
        return self.value

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        if vertex == self:
            print("A vertex cannot have an edge to itself")
            return
        
        self.edges[vertex.value] = weight
