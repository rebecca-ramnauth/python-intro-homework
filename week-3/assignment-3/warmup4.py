
number = int(input("Please enter a number:"))

# To check whether the number is positive, negative, or zero.
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# If the remainder after dividing by 2 is zero, the number is even.
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
