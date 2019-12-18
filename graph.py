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

    def find_path(self, start_vertex, end_vertex):
        print("Searching from {} to {}".format(start_vertex, end_vertex))
        start = [start_vertex]
        while len(start) > 0:
            current_vertex = start.pop(0)
            print(current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                start.extend(next_vertices)
        return False
