
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 17:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    decimal_integer = int(binary_representation, 2)
    if decimal_integer % fibonacci_sequence[16] == 0:
        return True
    else:
        return False
