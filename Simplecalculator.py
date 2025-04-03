num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation: +, -, *, /")
operation = input("Enter your choice: ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

print("Result:", result)
