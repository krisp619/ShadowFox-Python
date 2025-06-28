# Task 2: Numbers

# Part 1: Format 145 using 'o' (octal)
number = 145
formatted = format(number, 'o')
print("Formatted (octal) value of 145:", formatted)

# Part 2: Area of a circular pond and water calculation
radius = 84
pi = 3.14
area = pi * radius ** 2
print("Area of the pond:", area)

# Calculate total liters of water (1.4 liters per square meter)
water = area * 1.4
print("Total water in the pond (no decimal):", int(water))

# Part 3: Calculate speed in meters/second
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds
print("Speed in m/s (no decimal):", int(speed))
