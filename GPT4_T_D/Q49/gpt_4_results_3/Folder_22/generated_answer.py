
def if_decimal_is_divisible(bin_str):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

    def bin_to_dec(bin_str):
        return int(bin_str, 2)
        
    dec_num = bin_to_dec(bin_str)
    fib_20th = fib(20)
    
    return dec_num % fib_20th == 0
