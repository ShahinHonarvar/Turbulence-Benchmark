
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for _ in range(128):
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    return decimal % fibonacci_sequence[-1] == 0
