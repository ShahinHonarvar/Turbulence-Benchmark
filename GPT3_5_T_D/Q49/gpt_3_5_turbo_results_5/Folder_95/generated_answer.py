
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 169:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_int = int(binary_str, 2)
    return decimal_int % fibonacci_sequence[168] == 0
