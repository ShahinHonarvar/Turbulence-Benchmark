
def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]

    for i in range(2, 9):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    decimal_int = int(binary_string, 2)

    if decimal_int % fib_sequence[-1] == 0:
        return True
    else:
        return False
