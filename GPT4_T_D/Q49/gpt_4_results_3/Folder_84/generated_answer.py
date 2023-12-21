
def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_sequence = [0, 1]

    while len(fib_sequence) < 197:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return decimal % fib_sequence[-1] == 0
