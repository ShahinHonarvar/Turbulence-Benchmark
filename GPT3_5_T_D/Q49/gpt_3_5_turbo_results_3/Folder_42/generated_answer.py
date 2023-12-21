
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= 146:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)

    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci_sequence[145] == 0
