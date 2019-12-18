class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __repr__(self):
        return self.value

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight = 0):
        print("Adding edge to {}".format(vertex))
        self.edges[vertex.value] = weight
