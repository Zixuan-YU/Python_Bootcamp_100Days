from Day10_art import logo
from replit import clear

print(logo)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


restart = True
continue_calc = True

while restart:
    x = int(input('What is the first number?: '))
    org = x
    z = 0
    # methods = {'+': add, '-': sub, '*': 'mult', '/':div}
    continue_calc = True
    while continue_calc:
        print('+\n', '-\n', '*\n', '/\n')
        cal_method = input('Pick an operation: ')

        y = int(input('What is the next number?: '))
        if cal_method == '+':
            z = add(x, y)
        elif cal_method == '-':
            z = sub(x, y)
        elif cal_method == '*':
            z = mult(x, y)
        elif cal_method == '/':
            z = div(x, y)
        print("{} {} {} = {}".format(org, cal_method, y, z))
        response = input("Type 'y' to continue calculating with {}, or type 'n' to start a calculation: ".format(z))
        if response == 'y':
            continue_calc = True
            org = z
            x = z
        else:
            continue_calc = False
            clear()



