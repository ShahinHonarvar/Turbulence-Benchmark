
def if_decimal_is_divisible(bin_string):
    fib_46 = 1836311903
    decimal = int(bin_string, 2)
    return decimal % fib_46 == 0
