
def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]

    for _ in range(136):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    decimal_number = int(binary_string, 2)

    return decimal_number % fib_sequence[138] == 0
