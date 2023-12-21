
def if_decimal_is_divisible(binary_string):
    binary_integer = int(binary_string, 2)

    fib_sequence = [0, 1]
    for i in range(2, 140):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return binary_integer % fib_sequence[139] == 0
