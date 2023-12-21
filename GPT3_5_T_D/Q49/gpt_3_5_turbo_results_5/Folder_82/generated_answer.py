
def if_decimal_is_divisible(binary):
    fib_sequence = [0, 1]
    while len(str(fib_sequence[-1])) < len(binary):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    decimal = int(binary, 2)
    if fib_sequence[99] == 0:
        return decimal % 1 == 0
    else:
        return decimal % fib_sequence[99] == 0
