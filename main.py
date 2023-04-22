def basic_operators(first_number, second_number, action):
    if action == "*":
        print(first_number * second_number)
    elif action == "+":
        print(first_number + second_number)
    elif action == "-":
        print(first_number - second_number)
    elif action == "%":
        print(first_number % second_number)


def factorial(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    print(result)


def power_of_number(number, power):
    print(number ** power)


def division(num1, num2, action):
    print(num1 / num2)


while True:
    operator = input("\nPlease enter one of the following actions to perform:\n"
                     "( +, -, *, /, ^, %, ! ) or type 'exit' to quit. \n")

    if operator == 'exit':
        break

    elif operator in ['+', '-', '*', '%']:
        number_1 = float(input("Please enter the first number:\n"))
        number_2 = float(input("Please enter the second number:\n"))
        basic_operators(number_1, number_2, operator)

    elif operator == '/':
        number_1 = float(input("Please enter the first number:\n"))
        number_2 = float(input("Please enter the second number, other than ZERO:\n"))
        try:
            if number_1 != 0 and number_2 != 0:
                division(number_1, number_2, operator)
        except ZeroDivisionError:
            print('Zero division not possible')

    elif operator == "!":
        try:
            the_number = int(input("Please enter just ONE INTEGER number:\n"))
            if isinstance(the_number, int):
                factorial(the_number)
        except ValueError:
            print("The entered number should be an integer !!!\n")

    elif operator == "^":
        try:
            number = int(input("Please enter an integer number:\n"))
            power = int(input("Please enter the power - integer number:\n"))
            if isinstance(number, int) and isinstance(power, int):
                power_of_number(number, power)
        except ValueError:
            print("Please enter only integers numbers for the power !!!\n")
    else:
        print('Operation not allowed !!!\n')
