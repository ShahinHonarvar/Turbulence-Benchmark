
def if_decimal_is_divisible(bin_string):
    fib_sequence = [0, 1]
    for _ in range(15):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_int = int(bin_string, 2)
    return decimal_int % fib_sequence[-1] == 0
