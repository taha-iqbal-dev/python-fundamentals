print("---EVEN ODD CHECKER---")
# This code determines whether the input number is Even or Odd

number = int(input("Enter the number to check: "))
if number%2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# % (modulus) gives remainder
# Even numbers remainder 0 when divided by 2
# Odd numbers remainder 1 when divided by 2