def add(n, nn):
    return n + nn

def subtract(n, nn):
    return n - nn

def multiply(n, nn):
    return n * nn

def divide(n, nn):
    return n / nn


def calculator ():
    print("Simple Calculator")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")

    choose = input("Enter any Operation(1,2,3,4): ")
    if choose in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choose == '1':
            result = add(num1, num2)
        elif choose == '2':
            result = subtract(num1, num2)
        elif choose == '3':
            result = multiply(num1, num2)
        elif choose == '4':
            result = divide(num1, num2)

        print(f"Python Calculator Answer: {result}")

    else:
        print("Please enter the number which are asked.")



print("Welcome to the Calculator Game")
print(calculator())