
age = int(input("What is your age? "))

if age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 17:
    print("You are a teen.")
elif age >= 18 and age <= 64:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior.")
else:
    print("Invalid age.")
