import math

class DistanceHotel:
    def __init__(self, name, lat, lon, connections=None):
        self.name= name
        self.lat = lat
        self.lon = lon
        self.connections= connections if connections else []


park_cafe = DistanceHotel("Park Cafe", 51.5074, 3.1278,["Railway Station," "War Memorial"])
railway_station = DistanceHotel("Railway Station", 51.5074, 1.1278, ["War Memorial", "The Park Hotel"])


def calculate_distance(lat1, lon1, lat2,lon2):
    R = 6371

    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    lon1_rad = math.radians(lon1)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad -lat1_rad
    dlon = lon2_rad -lon1_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2 )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

origin = railway_station
destination = park_cafe

distance = calculate_distance(origin.lat, origin.lon, destination.lat, destination.lon)
print("Distance between", origin.name, "and", destination.name, "is", round(distance, 2), "km")