
def if_decimal_is_divisible(bin_str):
    bin_int = int(bin_str, 2)
    fib_sequence = [0, 1]
    fib_len = 2
    while fib_len < 68:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        fib_len += 1
    return bin_int % fib_sequence[-1] == 0
