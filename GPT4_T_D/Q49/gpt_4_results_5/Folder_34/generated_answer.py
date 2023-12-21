
def if_decimal_is_divisible(bin_str):
    fib = [0, 1]
    for i in range(2, 24):
        fib.append(fib[i-1] + fib[i-2])
   
    dec_num = int(bin_str, 2)
    
    if dec_num % fib[23] == 0:
        return True
    else:
        return False
