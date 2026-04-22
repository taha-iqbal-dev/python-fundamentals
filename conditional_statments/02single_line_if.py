# Ternary Conditional Expressions
# A ternary expression allows writing an if-else condition in a single line
# Syntax: <value_if_true> if <condition> else <value_if_false>


# Example 1: Direct decision-based output
# Taking user input and normalizing it (removing spaces + handling case sensitivity)
food = input("Enter food (Cake/Pizza/Burger): ").strip().lower()

# If user enters "cake" → sweet, otherwise → fast food
# Note: This assumes any non-cake input is fast food (no validation here)
print("You like sweet") if food == "cake" else print("You like fast food")


# Example 2: Assigning value using ternary expression
# Taking Yes/No input and normalizing it
food_choice = input("Do you want food (Yes/No): ").strip().lower()

# Assigning result based on condition
# If input is "yes" → "Served", otherwise → "Not served"
result = "Served" if food_choice == "yes" else "Not served"

# Displaying the result
print(result)

# .strip() → removes extra spaces
# .lower() → avoids case mismatch