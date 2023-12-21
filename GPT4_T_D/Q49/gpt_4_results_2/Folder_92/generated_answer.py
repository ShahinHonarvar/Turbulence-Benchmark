
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    seventh_fibonacci_number = 8
    if decimal_number % seventh_fibonacci_number == 0:
        return True
    else:
        return False
