
def if_decimal_is_divisible(bin_str):
    dec_int = int(bin_str, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 68:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return dec_int % fib_sequence[-1] == 0
