import os

# Print the current working directory
print(os.getcwd())

# Check if the expenses.csv file exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# Build and print the file path
file_path = os.path.join("..", "data", "expenses.csv")
print(file_path)