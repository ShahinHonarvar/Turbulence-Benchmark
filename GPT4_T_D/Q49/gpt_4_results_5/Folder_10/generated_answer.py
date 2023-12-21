
def if_decimal_is_divisible(binary_str):
    dec_num = int(binary_str, 2)
    fib_seq = [0, 1]
    
    while len(fib_seq) <= 88:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
    if dec_num % fib_seq[87] == 0:
        return True
    else:
        return False
