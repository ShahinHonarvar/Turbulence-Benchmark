
def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    for _ in range(188):
        fib_sequence.append(sum(fib_sequence[-2:]))
    decimal_representation = int(binary_str, 2)
    return decimal_representation % fib_sequence[188] == 0
