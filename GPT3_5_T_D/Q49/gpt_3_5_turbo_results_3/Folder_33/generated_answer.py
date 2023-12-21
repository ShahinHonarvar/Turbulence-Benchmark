
def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 135:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fib_sequence[134] == 0
