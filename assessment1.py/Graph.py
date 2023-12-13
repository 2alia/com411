from edge import Edge
from heapq import heappush
class Graph:
    def __init__(self):
        self.node_list = []
    def add_node(self, node):
        self.node_list.append(node)
    def add_edge(self, start, end , dist):
        forward_edge = Edge(start, end, dist)
        reverse_edge = Edge(end, start, dist)


        start.edges.append (forward_edge)
        end.edges.append (reverse_edge)

    def dijsktra(self, start, end):
        open_list = []
        start.dist = 0
        cur_node = start
        heappush(open_list, start)
        while cur_node != end and len(open_list) > 0:
                pass



