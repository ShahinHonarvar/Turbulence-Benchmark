
def if_decimal_is_divisible(bin_str):
    fib_seq = [0, 1]
    while(len(fib_seq) < 118):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
    dec_num = int(bin_str, 2)
    
    if dec_num % fib_seq[117] == 0:
        return True
    else:
        return False
