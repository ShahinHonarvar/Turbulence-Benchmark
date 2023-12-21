
def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 9:
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_sequence[8] == 0
