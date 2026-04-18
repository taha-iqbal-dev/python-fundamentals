# Checking type of Data inside variables

name = "Taha Iqbal"
age = 21
height = 5.7
is_student = True

#Now checking type of each variable

print("\n---DATA TYPE CHECKING---")

# type() function returns the class/type of a variable


print(f"Type of (name) is: {type(name)}")
print(f"Type of (age) is: {type(age)}")
print(f"Type of (height) is: {type(height)}")
print(f"Type of (is_student) is: {type(is_student)}")

# Better output
# adding ".__name__" along with type() prints only name of type alone

print("\n---Better Output---")
print(f"Type of (name) {name} is: {type(name).__name__}")
print(f"Type of (age) {age} is: {type(age).__name__}")
print(f"Type of (height) {height} is: {type(height).__name__}")
print(f"Type of (is_student) {is_student} is: {type(is_student).__name__}")