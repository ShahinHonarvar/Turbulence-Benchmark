
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < int(binary_representation, 2):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return int(binary_representation, 2) % fibonacci_sequence[9] == 0
