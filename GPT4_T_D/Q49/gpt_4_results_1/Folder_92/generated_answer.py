
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8]
    if decimal % fibonacci_sequence[6] == 0:
        return True
    else:
        return False
