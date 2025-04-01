# Basic Calculator Program

# Prompt user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt user to input the mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the selected operation and print the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operation! Please enter +, -, *, or /.")
