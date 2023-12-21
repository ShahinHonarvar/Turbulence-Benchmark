
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_195 = 677398962242828101
    return decimal_number % fib_195 == 0
