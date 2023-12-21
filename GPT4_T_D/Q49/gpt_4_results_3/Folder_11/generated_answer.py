
def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 16:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_sequence[15] == 0
