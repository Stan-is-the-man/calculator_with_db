def calculator(first_number, second_number, action):
    if action == "*":
        return first_number * second_number
    if action == "/":
        return first_number / second_number
    if action == "+":
        return first_number + second_number
    if action == "-":
        return first_number - second_number
    if action == "^":
        return first_number ^ second_number
    if action == "%":
        return first_number % second_number
    return 'Operation not allowed'


def factorial(number):
    result = 1
    for num in range(1, number + 1):
        result *= number
    return result


while True:
    operator = input("Please enter one of the following actions to perform:\n"
                     " +, -, *, /, ^, %, ! ")
    if operator != "!":
        number_1 = float(input("Please enter the first number"))
        number_2 = float(input("Please enter the second number"))
        calculator(number_1, number_2, operator)
    else:
        the_number = int(input("Please enter the first number"))
        factorial(the_number)
