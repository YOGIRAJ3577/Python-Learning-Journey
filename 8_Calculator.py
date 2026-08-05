a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = input("Enter the Operator (+, -, *, /,**): ")

if c == "+":
    print("The sum of two numbers is : ", a + b)
elif c == "-":
    print("The difference of two numbers is : ", a - b)
elif c == "*":
    print("The product of two numbers is : ", a * b)
elif c == "/":
    if b != 0:
        print("The division of two numbers is : ", a / b)
    else:
        print("Error: Division by zero is not allowed.")
elif c == "**":
    print("The result of exponentiation is : ", a ** b)
else:
    print("Error: Invalid operator.")