
import csv
import os
from datetime import datetime

# Build the path to the expenses CSV file
file_path = os.path.join("..", "data", "expenses.csv")

# Check if the expenses file exists
if not os.path.exists(file_path):
    print("Error: expenses.csv not found.")
else:
    # Open the expenses CSV file for reading
    with open(file_path, "r") as file:
        # Read each expense as a dictionary
        reader = csv.DictReader(file)

        # Create a list to store the expenses
        expenses = []

        # Loop through each expense in the CSV file
        for row in reader:
            # Convert the amount from a string to a float
            row["amount"] = float(row["amount"])

            # Add the expense dictionary to the list
            expenses.append(row)

    # Create a list to store only Food expenses
    food_expenses = []

    # Loop through all expenses
    for expense in expenses:
        # Check if the expense is in the Food category
        if expense["category"] == "Food":
            food_expenses.append(expense)

    # Start the total Food spending at zero
    total = 0

    # Add up the amounts of all Food expenses
    for expense in food_expenses:
        total += expense["amount"]

    # Get today's date and format it for the report
    today = datetime.now()
    date_string = today.strftime("%B %d, %Y")

    # Create the Food Expense Report file
    with open("food_report.txt", "w") as report:
        # Write the report heading
        report.write(f"Food Expense Report — generated {date_string}\n")

        # Loop through each Food expense
        for expense in food_expenses:
            # Write the date and amount of each Food expense
            report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")

        # Write the total amount spent on Food
        report.write(f"Total: ${total:.2f}\n")
