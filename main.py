# Python Calculator

def add(x, y):
    return x + y


while True:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    operation = int(input("Enter operation(1-5): "))
    result = 0

    if operation == 1:
        result = add(number1, number2)

    elif operation == 2:
        pass
    elif operation == 3:
        pass
    elif operation == 4:
        pass
    elif operation == 5:
        break
    else:
        print("Invalid operation")

    print("Result: ", result)

