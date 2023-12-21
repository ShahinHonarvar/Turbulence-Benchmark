
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for i in range(2, 128):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_int = int(binary_str, 2)
    if decimal_int % fibonacci_sequence[127] == 0:
        return True
    else:
        return False
