from data_structures.graph import Graph

graph = Graph()

graph.add_edge("New York", "London")
graph.add_edge("New York", "Cairo")
graph.add_edge("New York", "Tokyo")
graph.add_edge("London", "Dubai")
graph.add_edge("Cairo", "Kyiv")
graph.add_edge("Cairo", "Madrid")
graph.add_edge("London", "Madrid")
graph.add_edge("Buenos Aires", "New York")
graph.add_edge("Tokyo", "Buenos Aires")
graph.add_edge("Kyiv", "San Francisco")

print(graph.breadth_first_search("New York"))
