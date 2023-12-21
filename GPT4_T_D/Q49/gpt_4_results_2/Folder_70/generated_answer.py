
def if_decimal_is_divisible(binary_string):
    fib_number = 0
    fib_list = [0, 1]
    while len(fib_list) < 138:
        fib_number = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_number)

    decimal_number = int(binary_string, 2)
    return decimal_number % fib_list[137] == 0
