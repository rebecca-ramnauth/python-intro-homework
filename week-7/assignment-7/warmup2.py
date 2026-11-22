import csv

# Open the CSV file for reading
with open("../data/students.csv", "r") as file:
    # Read each row as a dictionary
    reader = csv.DictReader(file)

    # Print each student's name and score
    for student in reader:
        print(f"{student['name']}: {student['score']}")