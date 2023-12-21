
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = 2
    return decimal_number % fibonacci_number == 0
