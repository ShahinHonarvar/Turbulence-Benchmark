
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_list = [0, 1]
    while len(fib_list) < 188:
        fib_list.append(fib_list[-1] + fib_list[-2])
    if decimal_integer % fib_list[-1] == 0:
        return True
    return False
