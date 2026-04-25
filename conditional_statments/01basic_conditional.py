# Conditional Statments- shows results based on the given condition

print("---CONDITIONAL STATMENT---")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult") # Indentation needed
elif age >= 13:
    print("Your are a teenager")
else:
    print("You are underage")

# Note: invalid input (non-numeric) will cause an error
