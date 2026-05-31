import random

destinations = {
    "Goa": {
        "tags": ["beach", "nightlife", "relaxation"],
        "budget": "medium",
        "foods": ["Goan Curry", "Seafood Platter", "Bebinca"],
        "places": ["Baga Beach", "Fort Aguada", "Dudhsagar Falls"],
        "activities": ["Water Sports", "Boat Cruise", "Beach Walk", "Nightlife Tour"],
        "hotel": 3000,
        "food_cost": 1200,
        "travel_cost": 4000
    },
    "Manali": {
        "tags": ["mountain", "adventure", "nature"],
        "budget": "medium",
        "foods": ["Momos", "Trout Fish", "Himachali Thali"],
        "places": ["Solang Valley", "Rohtang Pass", "Hadimba Temple"],
        "activities": ["Paragliding", "Camping", "River Rafting", "Snow Activities"],
        "hotel": 2500,
        "food_cost": 1000,
        "travel_cost": 5000
    },
    "Jaipur": {
        "tags": ["history", "culture", "royal"],
        "budget": "low",
        "foods": ["Dal Baati", "Ghewar", "Laal Maas"],
        "places": ["Amber Fort", "Hawa Mahal", "City Palace"],
        "activities": ["Fort Tour", "Shopping", "Museum Visit", "Camel Ride"],
        "hotel": 2000,
        "food_cost": 900,
        "travel_cost": 3500
    },
    "Kerala": {
        "tags": ["nature", "relaxation", "backwaters"],
        "budget": "high",
        "foods": ["Appam", "Puttu", "Kerala Fish Curry"],
        "places": ["Alleppey", "Munnar", "Thekkady"],
        "activities": ["Houseboat Ride", "Tea Garden Visit", "Backwater Cruise", "Ayurvedic Spa"],
        "hotel": 4500,
        "food_cost": 1500,
        "travel_cost": 6000
    },
    "Ladakh": {
        "tags": ["adventure", "mountain", "nature"],
        "budget": "high",
        "foods": ["Thukpa", "Butter Tea", "Momos"],
        "places": ["Pangong Lake", "Nubra Valley", "Leh Palace"],
        "activities": ["Bike Expedition", "Trekking", "Lake Visit", "Monastery Tour"],
        "hotel": 5000,
        "food_cost": 1600,
        "travel_cost": 8000
    }
}

travel_tips = {
    "beach": ["Sunscreen", "Sunglasses", "Light Clothing"],
    "mountain": ["Jacket", "Trekking Shoes", "Thermal Wear"],
    "adventure": ["First Aid Kit", "Safety Gear", "Power Bank"],
    "history": ["Camera", "Guidebook", "Comfortable Footwear"],
    "nature": ["Binoculars", "Water Bottle", "Outdoor Wear"],
    "nightlife": ["Identity Card", "Casual Outfit", "Mobile Charger"],
    "culture": ["Camera", "Traditional Food Guide", "Walking Shoes"]
}

budget_rank = {
    "low": 1,
    "medium": 2,
    "high": 3
}

print("\n" + "=" * 60)
print("                 AI TRAVEL PLANNER")
print("=" * 60)

name = input("Enter your name: ")

interest = input(
    "Enter your interest (beach/mountain/history/adventure/nature/nightlife/culture): "
).lower()

budget = input(
    "Enter your budget (low/medium/high): "
).lower()

days = int(input("Enter number of travel days: "))

recommendations = []

for destination, details in destinations.items():

    score = 0

    if interest in details["tags"]:
        score += 3

    if budget_rank[budget] >= budget_rank[details["budget"]]:
        score += 2

    recommendations.append((score, destination))

recommendations.sort(reverse=True)

recommended_places = [
    destination
    for score, destination in recommendations
    if score > 0
]

if len(recommended_places) == 0:
    recommended_places = list(destinations.keys())

print("\nRecommended Destinations")
print("-" * 30)

for i, destination in enumerate(recommended_places, start=1):
    print(f"{i}. {destination}")

choice = int(input("\nSelect destination number: "))

selected_destination = recommended_places[choice - 1]

data = destinations[selected_destination]

hotel_total = data["hotel"] * days
food_total = data["food_cost"] * days
travel_total = data["travel_cost"]

total_cost = hotel_total + food_total + travel_total

print("\n" + "=" * 60)
print("              PERSONALIZED TOUR PLAN")
print("=" * 60)

print(f"\nTraveler      : {name}")
print(f"Destination   : {selected_destination}")
print(f"Duration      : {days} Days")
print(f"Interest      : {interest.title()}")

print("\nTourist Attractions")

for place in data["places"]:
    print("•", place)

print("\nFood Recommendations")

for food in data["foods"]:
    print("•", food)

print("\nRecommended Travel Essentials")

for item in travel_tips.get(interest, []):
    print("•", item)

print("\nDay-wise Itinerary")

activities = data["activities"].copy()
random.shuffle(activities)

for day in range(1, days + 1):
    activity = activities[(day - 1) % len(activities)]
    print(f"Day {day}: {activity}")

print("\nCost Assessment")
print("-" * 30)

print(f"Accommodation : Rs. {hotel_total}")
print(f"Food          : Rs. {food_total}")
print(f"Transportation: Rs. {travel_total}")
print(f"Total Cost    : Rs. {total_cost}")

print("\nAI Suggestions")
print("-" * 30)

if selected_destination == "Goa":
    print("Best season to visit: November to February")

elif selected_destination == "Ladakh":
    print("Spend a day acclimatizing before adventure activities")

elif selected_destination == "Kerala":
    print("Book houseboats in advance during peak season")

elif selected_destination == "Jaipur":
    print("Explore local markets for authentic handicrafts")

elif selected_destination == "Manali":
    print("Check weather conditions before adventure sports")

if budget == "low":
    print("Use public transport and budget accommodations to reduce expenses")

if interest == "adventure":
    print("Carry safety equipment and emergency supplies")

print("\nThank you for using our app and hope to see you again!")
