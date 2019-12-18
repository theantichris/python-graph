class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __repr__(self):
        return self.value

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        if vertex.value == self.value:
            print("A vertex cannot have an edge to itself")
        else:
            print("Adding edge to {}".format(vertex))
            self.edges[vertex.value] = weight
