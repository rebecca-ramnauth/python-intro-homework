while True:
    try:
        number = float(input("Enter a number: "))
        print(f"The number you entered is: {number}")
        break
    except ValueError:
        print("That's not a valid number. Try again.")