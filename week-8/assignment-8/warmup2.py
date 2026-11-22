num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    result = num1 / num2
    print(f"{num1} ÷ {num2} = {result:.2f}")
except ZeroDivisionError:
    print("Can't divide by zero. Please enter a non-zero number.")