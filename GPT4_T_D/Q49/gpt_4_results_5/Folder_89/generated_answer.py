
def if_decimal_is_divisible(binary_string):
    binary_string = int(binary_string, 2)
    fib_sequence = [0, 1]

    while len(fib_sequence) < 126:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    if binary_string % fib_sequence[125] == 0:
        return True
    else:
        return False
