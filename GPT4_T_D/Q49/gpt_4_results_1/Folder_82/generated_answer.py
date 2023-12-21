
def if_decimal_is_divisible(binary_input):
    decimal_input = int(binary_input, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 100:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if decimal_input % fib_sequence[99] == 0:
        return True
    else:
        return False
