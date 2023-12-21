
def if_decimal_is_divisible(binary_string):
    fib_list = [0, 1]
    while len(fib_list) < 128:
        fib_list.append(fib_list[-1] + fib_list[-2])
    decimal = int(binary_string, 2)
    return decimal % fib_list[127] == 0
