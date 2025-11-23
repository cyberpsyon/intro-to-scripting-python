# Name: Ben Mickens
# Due Date: 11-09-2025
# Description: A program to track travel plans using immutable tuples.

print("--- Travel Itinerary Tracker ---")

# Each tuple contains: (destination city, # of days staying, mode of transport)
trip1 = ("Houston", 7, "Car")
trip2 = ("Dallas", 5, "Airplane")
trip3 = ("Austin", 3, "Motorcycle")

# Add tuples to a list
itinerary = [trip1, trip2, trip3]

# Display all trips
print("\n--- Full Itinerary ---")
for city, days, mode in itinerary:
    print(f"Destination: {city} | Duration: {days} days | Travel: {mode}")

# Prompt user to lookup info for a trip
print("\n--- Trip Lookup ---")
choice = int(input("Enter the trip number you want to view (1-3): "))

if 1 <= choice <= 3:
    # Access the specific tuple using indexing
    selected_trip = itinerary[choice - 1]

    print(f"\nHere are the details for Trip #{choice}:")
    print(f"Result: {selected_trip}")
else:
    print("\nError: Invalid trip number entered.")