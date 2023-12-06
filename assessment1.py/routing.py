import math

class POI:
    def __init__(self, name, lat, lon, connections=None):
        self.name = name
        self.lat = lat  # Latitude
        self.lon = lon  # Longitude
        self.connections = connections if connections else []

# Define points of interest with geolocation data
railway_station = POI("Railway Station", 51.5074, 1.1278, ["Park Cafe", "War Memorial"])
park_cafe = POI("Park Cafe", 51.5074, 4.1278, ["Railway Station", "War Memorial", "The Park Hotel"])
# Add latitude and longitude for other points of interest...

# Function to calculate distance between two points using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers

    # Convert latitudes and longitudes from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula to calculate distance
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

# Example usage to calculate distance between two points
origin = railway_station
destination = park_cafe

distance = calculate_distance(origin.lat, origin.lon, destination.lat, destination.lon)
print("Distance between", origin.name, "and", destination.name, "is", round(distance, 2), "km")





