import time
import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='calculator_db',
    user='postgres',
    password='1123QwER'
)

cursor_object = connection.cursor()

cursor_object.execute(
    """CREATE TABLE IF NOT EXISTS calculator_statistics (
    id SERIAL PRIMARY KEY,
    action_type VARCHAR(10),
    results FLOAT,
    execution_time FLOAT
    )"""
)
connection.commit()


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
        start = time.time()
        basic_operators(number_1, number_2, operator)
        end = time.time()
        total_time = end - start

    elif operator == '/':
        number_1 = float(input("Please enter the first number:\n"))
        number_2 = float(input("Please enter the second number, other than ZERO:\n"))
        try:
            if number_1 != 0 and number_2 != 0:
                start = time.time()
                division(number_1, number_2, operator)
                end = time.time()
                total_time = end - start
        except ZeroDivisionError:
            print('Zero division not possible')

    elif operator == "!":
        try:
            the_number = int(input("Please enter just ONE INTEGER number:\n"))
            if isinstance(the_number, int):
                start = time.time()
                factorial(the_number)
                end = time.time()
                total_time = end - start
        except ValueError:
            print("The entered number should be an integer !!!\n")

    elif operator == "^":
        try:
            number = int(input("Please enter an integer number:\n"))
            power = int(input("Please enter the power - integer number:\n"))
            if isinstance(number, int) and isinstance(power, int):
                start = time.time()
                power_of_number(number, power)
                end = time.time()
                total_time = end - start
        except ValueError:
            print("Please enter only integers numbers for the power !!!\n")
    else:
        print('Operation not allowed !!!\n')
