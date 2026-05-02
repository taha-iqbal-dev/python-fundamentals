# Generates multiplication table for a given number up to a user-defined limit

n = int(input("Enter number whose table to be printed: "))
limit = int(input("Enter limit of table: "))

if limit < 0:
    print("Limit can't be NEGATIVE")
else:
    for i in range(1, limit+1):
        print(f"{n} X {i} = {n*i}")