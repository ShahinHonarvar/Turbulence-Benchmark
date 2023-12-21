
def if_decimal_is_divisible(binary_repr):
    fibonacci_sequence = (0, 1)
    for i in range(2, len(binary_repr)):
        fibonacci_sequence += (fibonacci_sequence[-1] + fibonacci_sequence[-2],)
    return int(binary_repr, 2) % fibonacci_sequence[150] == 0
