
def if_decimal_is_divisible(bin_str):
    fib_sequence = [0, 1]
    for i in range(2, 84):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        
    dec_num = int(bin_str, 2)
    
    if dec_num % fib_sequence[83] == 0:
        return True
    else:
        return False
