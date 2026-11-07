# Loop through numbers 1 to 30.
for number in range(1, 31):

    # Check if the number is divisible by both 3 and 5.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # Check if the number is divisible by 3.
    elif number % 3 == 0:
        print("Fizz")

    # Check if the number is divisible by 5.
    elif number % 5 == 0:
        print("Buzz")

    # Print the number if none of the conditions are met.
    else:
        print(number)