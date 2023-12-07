class node:
    def __init__(self, value):
        self.value =value
        self.adjacent_nodes = []

    def add_neighbour(self, neighbour_node):
        self.adjacent_nodes.append(neighbour_node)