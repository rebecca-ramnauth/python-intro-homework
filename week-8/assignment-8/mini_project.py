# Import the csv module to read and process CSV files
import csv

# Create empty lists to store valid data and skipped rows
clean_data = []
skipped_rows = []

# Initialize a counter to track the number of rows processed
row_number = 0

try:
    # Open the CSV file in read mode
    with open("../data/messy_data.csv", "r") as file:

        # Read the CSV file as dictionaries using column headers as keys
        reader = csv.DictReader(file)

        # Loop through each row and assign a row number
        for row_number, row in enumerate(reader, start=1):

            # Check for extra columns and skip the row if found
            if None in row:
                skipped_rows.append(f"Row {row_number}: extra column detected — skipped")
                continue

            try:
                # Check for missing names or categories
                if not row["name"] or not row["category"]:
                    skipped_rows.append(f"Row {row_number}: missing name or category — skipped")
                    continue

                # Convert the amount from a string to a float
                amount = float(row["amount"])

                # Store successfully parsed rows as dictionaries
                clean_data.append({
                    "name": row["name"],
                    "category": row["category"],
                    "amount": amount
                })

            # Handle amounts that cannot be converted to a number
            except ValueError:
                skipped_rows.append(f"Row {row_number}: ValueError — could not convert '{row['amount']}' to float")

            # Handle missing expected columns
            except KeyError:
                skipped_rows.append(f"Row {row_number}: KeyError — missing expected column")

    # Print the CSV report summary
    print("\n=== CSV Report ===")
    print(f"Rows attempted:  {row_number}")
    print(f"Rows parsed:     {len(clean_data)}")
    print(f"Rows skipped:    {len(skipped_rows)}")

    # Print the skipped rows and their errors
    print("\nSkipped rows:")
    for skipped in skipped_rows:
        print(f"  {skipped}")

    # Print the valid rows with amounts formatted to two decimal places
    print("\nClean data:")
    for row in clean_data:
        print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")

# Handle the error if the CSV file does not exist
except FileNotFoundError:
    print("Error: CSV file was not found. Please check the file path.")