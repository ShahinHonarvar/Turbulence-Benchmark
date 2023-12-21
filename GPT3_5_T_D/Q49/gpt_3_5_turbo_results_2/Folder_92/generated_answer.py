
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 7:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    decimal_integer = int(binary_string, 2)
    if decimal_integer % fibonacci_sequence[6] == 0:
        return True
    else:
        return False
