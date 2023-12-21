
def if_decimal_is_divisible(binary_str):
    decimal_integer = int(binary_str, 2)
    fib_sequence = [0, 1]
    for _ in range(2, 67):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    if decimal_integer % fib_sequence[-1] == 0:
        return True
    else:
        return False
