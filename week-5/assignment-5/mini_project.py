# List of numbers provided for the mini-project.
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
while True:
    # Print a line with spaces to separate each menu display.
    print("          ")
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    # Ask the user to choose an option.
    choice = input("Choose an option (1-5): ")

    # Exit the loop when the user selects option 5.
    if choice == "5":
        print("Goodbye!")
        break
    # Find the smallest number without using min().
    elif choice == "1":
        # Assume the first number is the minimum.
        minimum = numbers[0]

        # Compare each number with the minimum found so far.
        for number in numbers:
            if number < minimum:
                minimum = number

        # Display the minimum after checking all numbers.
        print(f"The minimum number is {minimum}.")
    # Find the largest number without using max().
    elif choice == "2":
        # Assume the first number is the maximum.
        maximum = numbers[0]

        # Compare each number with the maximum found so far.
        for number in numbers:
            if number > maximum:
                maximum = number

        # Display the maximum after checking all numbers.
        print(f"The maximum number is {maximum}.")
    # Search for a number in the list.
    elif choice == "3":
        # Ask the user which number to search for.
        search_number = int(input("Enter a number to search for: "))

        # Track whether the number has been found.
        number_found = False

        # Check each number and its index.
        for index, number in enumerate(numbers):
            if number == search_number:
                print(f"Found {search_number} at index {index}.")
                number_found = True
                break

        # Display a message if the number was not found.
        if not number_found:
            print(f"{search_number} was not found in the list.")
    # Sort the numbers from smallest to largest using bubble sort.
    elif choice == "4":
        # Keep sorting until no swaps are needed.
        swapped = True

        while swapped:
            # Assume no swaps will be needed during this pass.
            swapped = False

            # Compare each number with the one immediately after it.
            for index in range(len(numbers) - 1):
                if numbers[index] > numbers[index + 1]:
                    # Swap the two numbers.
                    numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                    swapped = True

        # Display the sorted list.
        print(f"Sorted list: {numbers}")