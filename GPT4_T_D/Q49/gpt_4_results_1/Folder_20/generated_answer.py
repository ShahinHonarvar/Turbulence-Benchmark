
def if_decimal_is_divisible(binary_str):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= 100:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_number = int(binary_str, 2)
    if decimal_number % fib_sequence[99] == 0:
        return True
    else:
        return False
