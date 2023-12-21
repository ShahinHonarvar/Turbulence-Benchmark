
def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 76:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_integer % fib_sequence[-1] == 0
