# match-case is used for pattern matching (alternative to multiple if-elif conditions)

print("---FOOD MENU---")

choice = input("Enter your choice (cake/pizza/burger): ").strip().lower()

match choice:
    case "cake":
        print("You chose a sweet ")
    case "pizza":
        print("You chose a fast food ")
    case "burger":
        print("You chose a fried food ")
    case _:
        print("Invalid choice")

# _ means: match anything (default case)