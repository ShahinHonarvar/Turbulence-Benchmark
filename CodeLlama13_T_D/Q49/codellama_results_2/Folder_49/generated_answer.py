
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = []
    a, b = 0, 1
    while a < int(binary_string):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return True if int(binary_string) % fibonacci_sequence[94] == 0 else False
