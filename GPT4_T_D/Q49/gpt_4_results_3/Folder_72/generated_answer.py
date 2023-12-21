
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    for _ in range(173):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    nth_fibonacci_number = fibonacci_sequence[174]
    decimal_number = int(binary_representation, 2)
    return decimal_number % nth_fibonacci_number == 0
