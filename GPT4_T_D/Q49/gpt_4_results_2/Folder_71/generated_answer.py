
def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)

    fib_list = [0, 1]
    while len(fib_list) <= 147:
        fib_list.append(fib_list[-1] + fib_list[-2])

    return number % fib_list[147] == 0
