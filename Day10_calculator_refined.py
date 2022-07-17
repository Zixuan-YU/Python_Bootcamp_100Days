from Day10_art import logo
from replit import clear

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

operations = {"+": add, "-": sub, "*": mult, "/":div}

def calculator():
    print(logo)
    num1 = float(input('What is the first number?: '))

    for k in operations:
        print(k)

    continue_calc = True

    while continue_calc:
        operation_symbol = input('Pick an operation: ')
        calculation_function = operations[operation_symbol]
        num2 = float(input('What is the next number?: '))

        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating with {}, or type 'n' to start a calculation: ".format(z)) == True:
            num1 = answer
        else:
            continue_calc = False
            clear()
            calculator()

calculator()