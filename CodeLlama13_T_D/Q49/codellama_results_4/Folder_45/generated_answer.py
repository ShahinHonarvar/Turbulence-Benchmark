
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = (0, 1)
    for i in range(2, 37):
        fibonacci_sequence += (fibonacci_sequence[-2] + fibonacci_sequence[-1],)
    decimal = int(binary_string, 2)
    return decimal % fibonacci_sequence[28] == 0
