
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 6:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    sixth_fibonacci = fibonacci_sequence[-1]
    return decimal % sixth_fibonacci == 0
