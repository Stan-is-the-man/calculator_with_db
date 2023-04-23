import time


def calculate_execution_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")


def factorial(number):
    result = 1

    for num in range(1, number + 1):
        result *= num
    return result


def add(a, b):
    return a + b




# calculate_execution_time(add(4, 6))
calculate_execution_time(factorial(123))


# print(factorial(5))


# calculate_execution_time(factorial(5))

# print(factorial(5))


# print(25%100)


# a = 5.5
# if isinstance(a, int):
#     print('Yes')
# else:
#     print('No')


# def time_for_execution(action):
#     start = time.time()
#     action
#     end = time.time()
#     total_time = end - start
#     print(total_time)
#
#
# a = int(input('Enter num 1\n'))
#
# factorial(a)
# time_for_execution(factorial(a))

# print(total_time)
