
def if_decimal_is_divisible(binary_string):
    binary_decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < binary_decimal:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return binary_decimal % fibonacci_sequence[26] == 0
