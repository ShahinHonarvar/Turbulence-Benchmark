
def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 39:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    thirty_nine_fib = fib_sequence[-1]
    return num % thirty_nine_fib == 0
