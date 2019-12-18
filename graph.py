class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding {}".format(vertex.value))
        self.graph_dict[vertex.value] = vertex