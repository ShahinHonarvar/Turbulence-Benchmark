
def if_decimal_is_divisible(bin_str):
    dec_num = int(bin_str, 2)
    
    fib_seq = [0, 1]
    for _ in range(183):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
    return dec_num % fib_seq[-1] == 0
