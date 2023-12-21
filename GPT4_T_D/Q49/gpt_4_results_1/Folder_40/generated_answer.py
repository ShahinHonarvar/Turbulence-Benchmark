
def if_decimal_is_divisible(binary_string):
    fibonacci_4th = 2
    decimal_num = int(binary_string, 2)
    if decimal_num % fibonacci_4th == 0:
        return True
    else:
        return False
