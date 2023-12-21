
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < 188:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    decimal_integer = int(binary_representation, 2)
    if decimal_integer % fibonacci_sequence[187] == 0:
        return True
    else:
        return False
