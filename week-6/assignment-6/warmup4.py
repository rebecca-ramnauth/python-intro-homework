def is_valid_score(score):
    # type() checks the data type of a value, such as int, str, or float.
    if type(score) is int and 0 <= score <= 100:
        return True
    else:
        return False

# Try to convert the user's input into an integer.
try:
    score = int(input("Enter a score: "))

    if is_valid_score(score):
        print("Valid score.")
    else:
        print("Invalid score — must be between 0 and 100.")

# Catch a ValueError if the input cannot be converted into an integer.
except ValueError:
    print("Invalid score — must be between 0 and 100.")