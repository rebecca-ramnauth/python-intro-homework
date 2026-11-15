# List of numbers provided for the mini-project.
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
#For option 1
def find_min(numbers):
    # Assume the first number is the minimum.
    minimum = numbers[0]

    # Compare each number with the minimum found so far.
    for number in numbers:
        if number < minimum:
            minimum = number

    # Return the smallest number after checking the list.
    return minimum

#For option 2
def find_max(numbers):
    # Assume the first number is the maximum.
    maximum = numbers[0]

    # Compare each number with the maximum found so far.
    for number in numbers:
        if number > maximum:
            maximum = number

    # Return the largest number after checking the list.
    return maximum

#For option 3
def search(numbers, target):
    # Check each number and its index.
    for index, number in enumerate(numbers):
        if number == target:
            return index

    # Return -1 if the target is not found in the list.
    return -1

#For option 4
def bubble_sort(numbers):
    # Create a copy so the original list stays unchanged.
    sorted_numbers = numbers.copy()

    # Keep sorting until no swaps are needed.
    swapped = True

    while swapped:
        # Assume no swaps will be needed during this pass.
        swapped = False

        # Compare each number with the one immediately after it.
        for index in range(len(sorted_numbers) - 1):
            if sorted_numbers[index] > sorted_numbers[index + 1]:
                # Swap the two numbers.
                sorted_numbers[index], sorted_numbers[index + 1] = sorted_numbers[index + 1], sorted_numbers[index]
                swapped = True

    # For new option 5. Return the new sorted list.
    return sorted_numbers
def show_menu():
    # Display the Number Cruncher menu.
    print("          ")
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    # Ask the user to choose an option.
    choice = input("Choose an option (1-5): ")

    return choice
def main():
    while True:
        choice = show_menu()

        if choice == "5":
            print("Goodbye!")
            break

        elif choice == "1":
            minimum = find_min(numbers)
            print(f"The minimum number is {minimum}.")
        elif choice == "2":
            maximum = find_max(numbers)
            print(f"The maximum number is {maximum}.")
        elif choice == "3":
            search_number = int(input("Enter a number to search for: "))
            index = search(numbers, search_number)

            if index != -1:
                print(f"Found {search_number} at index {index}.")
            else:
                print(f"{search_number} was not found in the list.")

        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print(f"Sorted list: {sorted_numbers}")
        else:
            print("Invalid choice. Please choose an option from 1 to 5.")

# Calls the function.
main()