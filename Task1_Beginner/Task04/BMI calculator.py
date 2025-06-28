# Task 04 - Part 1: BMI Calculator

# Get user input
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine category
if bmi >= 30:
    category = "Obesity"
elif bmi >= 25:
    category = "Overweight"
elif bmi >= 18.5:
    category = "Normal"
else:
    category = "Underweight"

# Output result
print(f"Your BMI is {bmi:.2f}. Category: {category}")
