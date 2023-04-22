def factorial(number):
    result = 1

    for num in range(1, number + 1):
        result *= num
    return result


# print(factorial(5))


# print(25%100)


# a = 5.5
# if isinstance(a, int):
#     print('Yes')
# else:
#     print('No')


import time


def time_for_execution(action):
    start = time.time()
    action
    end = time.time()
    total_time = end - start
    print(total_time)


a = int(input('Enter num 1\n'))

factorial(a)
time_for_execution(factorial(a))

# print(total_time)
