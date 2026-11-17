# Open the text file for reading
with open("../data/notes.txt", "r") as file:
    # Start counting lines from 1
    line_count = 1

    # Read and print each line with its number
    for line in file:
        line = line.strip()
        print(f"Line {line_count}: {line}")
        line_count += 1