
def if_decimal_is_divisible(binary_string):
    fibonacci_64 = 10610209857723
    decimal_number = int(binary_string, 2)
    if decimal_number % fibonacci_64 == 0:
        return True
    else:
        return False
