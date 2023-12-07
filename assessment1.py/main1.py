from  Node import node

node_a = node ("railway_station")
node_b = node ("park_hotel")
node_c = node ("war_memorial")

node_a.add_neighbour(node_b)
node_a.add_neighbour(node_c)
node_b.add_neighbour(node_c)
node_c.add_neighbour(node_b)
node_c.add_neighbour(node_a)

print(f"Node A's neighbour:{[node.value for node in node_a.adjacent_nodes]}")
print(f"Node B's neighbours:{[node.value for  node in node_b.adjacent_nodes]}")
print(f"Node C's neighbours: {[node.value for node in node_c.adjacent_nodes]}")
