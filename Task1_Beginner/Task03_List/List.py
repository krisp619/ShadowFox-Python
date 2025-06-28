# Task 3: List Operations with Custom Justice League

# Initial custom list
justice_league = ["Superman", "Shaktiman", "Ironman", "Thor", "Batman", "Spiderman"]
print("Initial list:", justice_league)

# Step 1: Count members
print("Number of members:", len(justice_league))

# Step 2: Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# Step 3: Move 'Shaktiman' to the beginning (assuming he's the leader now)
justice_league.remove("Shaktiman")
justice_league.insert(0, "Shaktiman")
print("Shaktiman moved to the beginning:", justice_league)

# Step 4: Insert 'Ironman' between Batman and Spiderman
justice_league.remove("Ironman")
batman_index = justice_league.index("Batman")
justice_league.insert(batman_index + 1, "Ironman")
print("Ironman placed between Batman and Spiderman:", justice_league)

# Step 5: Replace the list with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

# Step 6: Sort the list alphabetically and show new leader
justice_league.sort()
print("Sorted team:", justice_league)
print("New leader (index 0):", justice_league[0])
