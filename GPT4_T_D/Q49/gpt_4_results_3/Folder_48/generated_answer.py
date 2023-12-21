
def if_decimal_is_divisible(binary_string):
    binary_to_decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= 198:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return binary_to_decimal % fibonacci_sequence[198] == 0
