def factorial(number):
    result = 1

    for num in range(1, number + 1):
        result *= number
    return result


print(factorial(5))

