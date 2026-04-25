print("---EVENT ENTRY SYSTEM---")
# This program decides whether a person is allowed to enter an event

age = int(input("Enter your age: "))
membership = input("Have you purchased ticket (Yes/No): ").strip().lower()
# strip() removes extra spaces
# lower() makes input case-insensitive (e.g., YES, yes, Yes → all become "yes")

if age >= 18:
    if membership == "yes":
        print("You are allowed to enter...")
    else:
        print("You're not allowed to enter...")
else:
    print("You are under age")