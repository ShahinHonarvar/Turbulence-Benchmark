
def if_decimal_is_divisible(binary_string):
    fib_46 = 1836311903
    decimal_int = int(binary_string, 2)
    return decimal_int % fib_46 == 0
