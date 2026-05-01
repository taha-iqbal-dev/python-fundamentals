# String Methods Demonstration

text = "  hello World  "

print(f"Original: '{text}'")

# Convert entire string to uppercase
print(f"Upper: {text.upper()}")

# Capitalize first character, rest become lowercase
print(f"Capitalize: {text.capitalize()}")

# Convert entire string to lowercase
print(f"Lower: {text.lower()}")

# Remove leading and trailing spaces
print(f"Strip: '{text.strip()}'")

# Replace substring (case-sensitive)
print(f"Replace: {text.replace('World', 'Python')}")

# Split string into list based on spaces
print(f"Split: {text.split()}")
