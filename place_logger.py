import json

# Initialize empty list to store places
places = []

# Prompt the user to enter a place
while True:
    place = input("Enter a place (or type 'done' to finish): ")
    if place.lower() == 'done':  # Exit condition
        break
    places.append(place)

# Convert list to JSON object
places_json = json.dumps(places, indent=2)

# Display all places in JSON format
print("Here are all the places you entered in JSON format:")
print(places_json)
