graph = {}

nodes = ["railway_station","park_cafe", "war_memorial","park_hotel"]

for node in nodes:
    graph[node] = []


edges = [("railway_station","park_cafe"), ("railway_station", "park_hotel"),("park_cafe", "war_memorial"), ("park_hotel","park_hotel" )]
for edge in edges:
    source,destination = edge

    graph[source].append(destination)
    graph[destination].append(source)

for node in graph:
    print(f"Node {node}: {graph[node]}")