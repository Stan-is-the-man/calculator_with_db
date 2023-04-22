def calculator(first_number, second_number, action):
    if action == "*":
        print(first_number * second_number)
    elif action == "/":
        print(first_number / second_number)
    elif action == "+":
        print((first_number + second_number))
    elif action == "-":
        print(first_number - second_number)
    elif action == "^":
        print(first_number ^ second_number)
    elif action == "%":
        print(first_number % second_number)


def factorial(number):
    result = 1
    for num in range(1, number + 1):
        result *= num
    print(result)


while True:
    operator = input("Please enter one of the following actions to perform:\n"
                     "( +, -, *, /, ^, %, ! ) or type 'exit' to quit. \n")

    if operator == 'exit':
        break

    elif operator in ['+', '-', '*', '/', '%']:
        number_1 = float(input("Please enter the first number\n"))
        number_2 = float(input("Please enter the second number\n"))
        calculator(number_1, number_2, operator)

    elif operator == "!":
        the_number = int(input("Please enter just one number\n"))
        factorial(the_number)
    else:
        print('Operation not allowed:')
