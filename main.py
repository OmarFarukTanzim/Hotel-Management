class Room:
    def __init__(self, room_number, room_type, price, amenities):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.amenities = amenities  # List of amenities (e.g., Wi-Fi, air conditioning)
    def __repr__(self):
        return f"Room {self.room_number}: {self.room_type}, Price: ${self.price},      Amenities: {', '.join(self.amenities)}"

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []  # List to store available rooms

    def add_room(self, room):
        self.rooms.append(room)

    def get_available_rooms(self):
        return self.rooms

class Customer:
    def __init__(self, budget, preferred_room_type, required_amenities):
        self.budget = budget
        self.preferred_room_type = preferred_room_type
        self.required_amenities = required_amenities

    def filter_rooms(self, rooms):
        matching_rooms = [
            room for room in rooms
            if room.price <= self.budget
            and (self.preferred_room_type.lower() in room.room_type.lower() or self.preferred_room_type == "")
            and all(amenity in room.amenities for amenity in self.required_amenities)
        ]
        return matching_rooms

    def offer_room(self, hotel):
        available_rooms = hotel.get_available_rooms()
        filtered_rooms = self.filter_rooms(available_rooms)
        if not filtered_rooms:
            print("No rooms match your criteria. Please adjust your preferences.")
        else:
            print(f"\nHere are the rooms that match your preferences (Price <= ${self.budget}, Preferred Room Type: {self.preferred_room_type}, Amenities: {', '.join(self.required_amenities)}):")
            for room in filtered_rooms:
                print(room)





# Example usage:
# Create a hotel
hotel = Hotel("Ocean View Hotel")
# Add rooms to the hotel
hotel.add_room(Room(101, "Single", 100, ["Wi-Fi", "Air Conditioning", "TV"]))
hotel.add_room(Room(102, "Double", 150, ["Wi-Fi", "Air Conditioning", "TV", "Minibar"]))
hotel.add_room(Room(103, "Suite", 250, ["Wi-Fi", "Air Conditioning", "TV", "Minibar", "Ocean View"]))
hotel.add_room(Room(104, "Single", 90, ["Wi-Fi", "TV"]))
hotel.add_room(Room(105, "Double", 200, ["Wi-Fi", "Air Conditioning", "TV", "Minibar", "Balcony"]))
# Customer inputs preferences
print("Welcome to the hotel! Please provide your preferences:\n")

try:
    budget = float(input("Enter your budget (in USD): $"))
    preferred_room_type = input("Enter your preferred room type (Single, Double, Suite, or leave blank for any): ")
    required_amenities = input("Enter the amenities you require (comma separated, e.g., Wi-Fi, TV): ").split(",")
    required_amenities = [amenity.strip() for amenity in required_amenities]
    # Create a customer object
    customer = Customer(budget, preferred_room_type, required_amenities)
    # Offer rooms based on customer's preferences
    customer.offer_room(hotel)
except ValueError:
    print("Invalid input! Please enter valid numbers for budget.")
