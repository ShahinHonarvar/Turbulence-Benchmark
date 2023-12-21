
def if_decimal_is_divisible(bin_str):
    fib_sequence = [0, 1]
    while fib_sequence[-1] <= int(bin_str, 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return int(bin_str, 2) % fib_sequence[110] == 0
