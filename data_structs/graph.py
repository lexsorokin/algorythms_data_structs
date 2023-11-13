# Graph consist of nodes and edges (which connects the nodes)
# Difference between tree and graph - in tree there should be only one path between two nodes
# Weighted graph is the graph that have a certain weight for the edges (for example distance between cities that are represented in the nodes)
# One way that u can represent graph is a pair of nodes

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        # getting all possible paths from start to end (using recursion)
        path = path + [start]
        if start == end:  # simplest case if your starting point is also the end point
            return [path]
        if start not in self.graph_dict:
            # case where node has no edges originating from it only coming to it (basically if it serves only as a child)
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:  # checking if it visited or not
                # ['Dubai', 'New York']
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):

        path = path + [start]  # recursive function

        # case where node has no edges originating from it only coming to it (basically if it serves only as a child)
        if start not in self.graph_dict:
            return None

        if start == end:  # New York to New York
            return path

        shortest_path = None

        for node in self.graph_dict[start]:
            # some times can return None
            sp = self.get_shortest_path(node, end, path)
            if sp:
                # if shortest path is not initialized or new shortest path is shorter that an existing one
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp

        return shortest_path


routes = [
    ("Mumbai", "Paris"),  # one route
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

route_graph = Graph(routes)

# start = "Mumbai"
# start = "Toronto"
start = "Mumbai"
end = "New York"

print(route_graph.get_paths(start=start, end=end))
print(route_graph.get_shortest_path(start=start, end=end))

# d = {
#     "Mumbai": ["Paris", "Dubai"],
#     "Paris": ["Dubai", "New York"],
# }

# first step - transform from array data structure to hash table data structure
