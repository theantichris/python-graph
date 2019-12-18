class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding {}".format(vertex.value))
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        print("Adding edge from {} to {}".format(from_vertex, to_vertex))
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
          self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
