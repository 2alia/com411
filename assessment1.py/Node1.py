import sys
class Node:
    def __init__(self, name):
        self.name: name
        self.dist = sys.maxsize
        self.edges = []
        self.parent = None
        self.addToOpenList = False
    def __lt__(self, other_node):
        return  self.name < other_node.name
