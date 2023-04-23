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
    global result, total_time
    start = time.time()
    if action == "*":
        result = first_number * second_number
    elif action == "+":
        result = first_number + second_number
    elif action == "-":
        result = first_number - second_number
    elif action == "%":
        result = first_number % second_number
    elif action == '^':
        result = first_number ** second_number
    elif action == '/':
        result = first_number / second_number

    end = time.time()
    total_time = end - start

    print(result)

    cursor_object.execute("""
    INSERT INTO calculator_statistics(action_type, results,execution_time) 
    VALUES(%s, %s, %s)
        """, (action, result, total_time))
    connection.commit()


def factorial(number):
    action = "!"
    the_start = time.time()
    the_result = 1
    for num in range(1, number + 1):
        the_result *= num
    the_end = time.time()
    the_total_time = (the_end - the_start) * 100

    cursor_object.execute("""
        INSERT INTO calculator_statistics(action_type, results,execution_time) 
        VALUES(%s, %s, %s)
            """, (action, result, the_total_time))

    connection.commit()
    print(result)


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
                start = time.time()
                basic_operators(number_1, number_2, operator)
                end = time.time()
                total_time = end - start
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
                start = time.time()
                basic_operators(number, power, operator)
                end = time.time()
                total_time = end - start
        except ValueError:
            print("Please enter only integers numbers for the power !!!\n")
    else:
        print('Operation not allowed !!!\n')
