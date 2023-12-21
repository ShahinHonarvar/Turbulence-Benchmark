
def if_decimal_is_divisible(bin_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 77:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    dec_integer = int(bin_string, 2)
    
    if dec_integer % fib_sequence[76] == 0:
        return True
    else:
        return False
