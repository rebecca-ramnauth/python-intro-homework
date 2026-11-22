# Keep asking for input until a valid positive integer is entered.
while True:
    # Ask the user for a number. input() stores the entry as a string.
    entry = input("Enter a positive integer: ")

    # Check that the entry contains only digits and is greater than zero.
    # .isdigit() checks whether the input contains only digits.
    if entry.isdigit() and int(entry) > 0:
        print(f"Got it: {entry}")
        # Exit the while loop once a valid entry is received.
        break
    else:
        print("That's not a positive integer. Try again.")