# Simple Travel Itinerary - Array Update Practice

# Create array and input 5 destinations
places = []
print("Enter 5 travel destinations:")
for i in range(1, 6):
    places.append(input(f"Place {i}: "))

# Show original list
print("\nOriginal List:")
for i in range(5):
    print(f"{i+1}. {places[i]}")

# Update 2nd and 5th places (indices 1 and 4)
print("\n--- Updating ---")
places[1] = input("New destination #2: ")
places[4] = input("New destination #5: ")

# Show updated list
print("\nUpdated List:")
for i in range(5):
    print(f"{i+1}. {places[i]}")

print("\nYour itinerary is updated!")
