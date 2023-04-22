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

a = int(input('Enter num 1\n'))
# b = int(input('Enter num 2\n'))

start = time.time()
factorial(a)
end = time.time()
total_time = end - start
print(total_time)

