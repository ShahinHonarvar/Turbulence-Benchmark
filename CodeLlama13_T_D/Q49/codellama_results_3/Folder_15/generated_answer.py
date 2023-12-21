
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    decimal_number = int(binary_representation, 2)
    if decimal_number % fibonacci_sequence[9] == 0:
        return True
    else:
        return False
