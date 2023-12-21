
def if_decimal_is_divisible(bin_str):
    fib_sequence = [0, 1]
    for i in range(2, 10):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    decimal_integer = int(bin_str, 2)
    if decimal_integer % fib_sequence[9] == 0:
        return True
    else:
        return False
