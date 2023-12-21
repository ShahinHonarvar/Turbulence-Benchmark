
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 56:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fibonacci_number = fib_sequence[-1]
    return decimal % fibonacci_number == 0
