def route_function_hotel(self, hotel_name, destination):
    # Simulated directions
    directions = {
        'train station': 'take a right from the hotel, walk straight for 10 minutes, and you will find the train station.',
        'park': 'the nearest park is 5 minutes away from the hotel. Go left and walk until you see the park entrance.',
        'cafe': 'there is a cafe nearby. walk straight, and you will find it',
        'war memorial': 'head straight. Then turn left from the main road. finally in 15 minutes  you will reach it.',
        'car park': 'the car park will be opposite to the hotel. you can park your car there.'
    }
    if hotel_name.lower() == 'all':
        for destination_name, directions in directions.items():
            if destination.lower() in destination_name:
                print(f"Directions to {hotel_name} : {destination_name}")
                break
    else:
        for destination_name, directions in directions.items():
            if destination.name.lower() == destination.lower():
                print(f"directions from {hotel_name} to {destination_name}")
                break
        else:
            print(f"destination '{destination}' not found.")