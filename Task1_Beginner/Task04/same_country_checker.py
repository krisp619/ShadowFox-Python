# Task 04 - Part 3: Check if two cities are in the same country

# Country-city mappings
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# User input
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

# Function to get country of a city
def get_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

# Check countries
country1 = get_country(city1)
country2 = get_country(city2)

# Decision logic
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}.")
    else:
        print(f"{city1} is in {country1}, and {city2} is in {country2}. They don't belong to the same country.")
else:
    print("One or both cities are not in our database.")
