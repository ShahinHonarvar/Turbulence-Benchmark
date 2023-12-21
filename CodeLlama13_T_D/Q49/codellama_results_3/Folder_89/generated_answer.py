
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = (0, 1)
    for i in range(2, 100):
        fibonacci_sequence += (fibonacci_sequence[-2] + fibonacci_sequence[-1],)
    decimal = int(binary_str, 2)
    return decimal % fibonacci_sequence[126] == 0
