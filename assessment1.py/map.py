
# Representing points of interest as nodes in a graph
class POI:
    def __init__(self, name, connections=None):
        self.name = name
        self.connections = connections if connections else []

# Sample points of interest
railway_station = POI("Railway Station", ["Park Cafe", "War Memorial"])
park_cafe = POI("Park Cafe", ["Railway Station", "War Memorial", "The Park Hotel"])
war_memorial = POI("War Memorial", ["Park Cafe", "The Park Hotel"])
the_park_hotel = POI("The Park Hotel", ["Park Cafe", "War Memorial", "White Horse Pub"])
white_horse_pub = POI("White Horse Pub", ["The Park Hotel"])

# Create a map of points of interest
poi_map = {
    "Railway Station": railway_station,
    "Park Cafe": park_cafe,
    "War Memorial": war_memorial,
    "The Park Hotel": the_park_hotel,
    "White Horse Pub": white_horse_pub
}
from collections import deque

def find_route(origin, destination):
    visited = set()
    queue = deque([(origin, [])])

    while queue:
        current, path = queue.popleft()
        if current == destination:
            return path + [current]

        if current not in visited:
            visited.add(current)
            for neighbor in poi_map[current].connections:
                queue.append((neighbor, path + [current]))

    return None

# Example usage
origin = "Railway Station"
destination = "White Horse Pub"
route = find_route(origin, destination)

if route:
    print("Route from", origin, "to", destination, ":")
    for place in route:
        print("-", place)
else:
    print("No route found between", origin, "and", destination)

