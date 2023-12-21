
def if_decimal_is_divisible(binary_str):
    decimal_integer = int(binary_str, 2)
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(187):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return decimal_integer % fibonacci_sequence[186] == 0
