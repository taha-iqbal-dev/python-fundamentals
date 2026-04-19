# Taking multiple input at same time

print("---MULTIPLE INPUT HANDLING---")
name, father_name = input("Enter your name and your father name with space: ").split()
age, father_age = input("Enter your age and your father age with space: ").split()
# split() breaks the input into separate parts based on space
# Note: This will break if user does not enter exactly two values

age = int(age)
father_age = int(father_age)
# By default age & father_age were strings so type casting happened

print(f"\n Your name: {name}\n Your age: {age}\n Father name: {father_name}\n Father age: {father_age}")
