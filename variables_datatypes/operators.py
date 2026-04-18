# Use of Operators 

# Initial variables
a = 4
b = 2

# Arithmetic Operators- used for basic mathematical operations
print("---ARITHMETIC OPERATORS---")
print(f"Two variables a={a} and b={b}")
print("Addition (a + b):", a + b)        
print("Subtraction (a - b):", a - b)     
print("Multiplication (a * b):", a * b) 
print("Division (a / b):", a / b)        
print("Floor Division (a // b):", a // b) 
print("Modulus (a % b):", a % b)         
print("Exponent (a ** b):", a ** b)      

# Relaional  Operators- used for comparisons
print("\n---RELATIONAL OPERATORS---")
print(f"Two variables a={a} and b={b}")
print("a == b:", a == b)   # Equal
print("a != b:", a != b)   # Not equal
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal
print("a <= b:", a <= b)   # Less than or equal

# Logical Operators- used to combine conditional values either true or false
print("\n---LOGICAL OPERATORS---")
x = True
y = False
print(f"Two variables where x is {x} & y is {y}")
print("x AND y:", x and y)  # True only if both True
print("x OR y:", x or y)    # True if at least one True
print("NOT x:", not x)      # Reverse the value

# Assignment Operators - used to assign values
print("\n---ASSIGNMENT OPERATOR---")
c = 5
print("Initial c:", c)
c += 2   # c = c + 2
print("c += 2:", c)
c -= 1   # c = c - 1
print("c -= 1:", c)
c *= 3   # c = c * 3
print("c *= 3:", c)
c /= 2   # c = c / 2
print("c /= 2:", c)

print("\n---Type Insight---")
print("Type of a + b:", type(a + b))
print("Type of a / b:", type(a / b))  # important: division gives float