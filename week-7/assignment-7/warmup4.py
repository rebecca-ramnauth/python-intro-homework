from datetime import datetime

# Get the current date and time
today = datetime.now()

# Format the date as Month Day, Year
date_string = today.strftime("%B %d, %Y")

# Print today's date
print(f"Today is {date_string}.")