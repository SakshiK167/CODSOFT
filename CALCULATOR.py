def calculator():
    firstnum=int(input("Enter first number:"))
    secondnum=int(input("Enter second number:"))

    print("Select Operation to perform :")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")

    operation=input("Enter the operation(+,-,/,*)")

    if operation == '+':
        result = firstnum + secondnum
    elif operation == '-':
        result = firstnum - secondnum
    elif operation == '*':
        result = firstnum * secondnum
    elif operation == '/':
        if secondnum!= 0:
         result = firstnum / secondnum
        else:
         return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."


    return "The result is: {result}"

print(calculator())