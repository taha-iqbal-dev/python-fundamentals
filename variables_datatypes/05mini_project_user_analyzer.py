# User information analyzer
# Demonstrate: Variables, Data type, Type casting & Basic operation

name = input("Enter your name: ")
age = int(input("Enter your age (in years): "))
height = float(input("Enter your height (in feet): "))
current_year = int(input("Enter current year: "))

# Processing data
age_in_month = age*12
height_in_cm = height*30.48
birth_year = current_year-age
is_adult = age>=18

# Results
print("\n---USER PROFILE---")
print(f"Name: {name}")
print(f"Age in years: {age}")
print(f"Age in months: {age_in_month}")
print(f"Birth year: {birth_year}")
print(f"Is user and ADULT? {is_adult}")
print(f"Height in feet: {height}")
print(f"Height in centimeters: {height_in_cm}")
