# Represent a directed weighted graph and implement the Bellman-Ford
# Algorithm for computing the Single-Source Shortest Path of a graph.

# A class to give the Graph
class Bellman_Ford:
    def __init__(self, nodes):
        self.id = nodes  # Numbers of nodes
        self.arcs = []

    # A function that add the edges to the graph
    def add_edge(self, target, weight):
        self.arcs.append((target, weight))


# A Function provides a basic structure for representing a graph and adding vertices and edges to it
class Graph:
    def __init__(self):
        self.vertices = {}

    # A function that add the nodes to the graph
    def add_vertex(self, id):
        if id not in self.vertices:
            self.vertices[id] = Bellman_Ford(id)

    # A function that add the edges to the graph
    def add_edge(self, source, target, weight):
        if source in self.vertices and target in self.vertices:
            self.vertices[source].add_edge(target, weight)


# A function that finds shortest distances from source to
# all other nodes using Bellman-Ford algorithm.
# The function also detects negative weight cycle
def bellman_ford(graph, source):
    # Phase 1: Initialization (distances from source to other vertices/nodes)
    distances = {v: float('inf') for v in graph.vertices}
    distances[source] = 0

    # Pase 2: Relaxation of all arcs (A simple shortest
    # path from the source to any other vertex can have
    # at-most |V| - 1 edges)
    for _ in range(len(graph.vertices) - 1):
        for vertex in graph.vertices.values():
            for target, weight in vertex.arcs:
                if distances[vertex.id] + weight < distances[target]:
                    distances[target] = distances[vertex.id] + weight

    # Phase 3: Check for negative cycles (guarantees shortest
    # distances if graph doesn't contain
    # negative weight cycle.)

    for vertex in graph.vertices.values():
        for target, weight in vertex.arcs:
            if distances[vertex.id] + weight < distances[target]:
                raise ValueError("The Graph have negative cycle")
    return distances


# Print the distances between them
graph = Graph()

# Add vertices
graph.add_vertex("K10")
graph.add_vertex("K20")
graph.add_vertex("K30")
graph.add_vertex("K40")
graph.add_vertex("K50")

# Add arcs
graph.add_edge("K10", "K20", 5)
graph.add_edge("K10", "K30", 2)
graph.add_edge("K20", "K30", 1)
graph.add_edge("K20", "K40", 4)
graph.add_edge("K30", "K40", 7)
graph.add_edge("K30", "K50", 9)
graph.add_edge("K40", "K50", 11)

# Bellman function call
source_vertex = "K10"
distances = bellman_ford(graph, source_vertex)

print("Shortest distances from vertex", source_vertex)
for vertex, distance in distances.items():
    print("Bellman_Ford:", vertex, "Distance:", distance)
