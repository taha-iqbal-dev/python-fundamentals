# Code to check which number from given three is largest
print("---LARGEST NUMBER CHECKER---")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 and num2 == num3:
    print("All numbers are equal")

elif num1 >= num2 and num1 >= num3:
    print(f"{num1} is Largest")

elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is Largest")

else:
    print(f"{num3} is Largest")

