# Task 1: Variables

# Part 1: Store pi and check type
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

# Part 2: Trying to use reserved keyword as variable name (this will throw an error if uncommented)
# for = 4
# print(for)

# Fixed version:
for_value = 4
print("Value of 'for_value':", for_value)

# Part 3: Simple Interest Calculation
principal = 5000  # in currency units
rate = 7  # in percentage
time = 3  # in years

simple_interest = (principal * rate * time) / 100
print("Simple Interest for 3 years is:", simple_interest)
