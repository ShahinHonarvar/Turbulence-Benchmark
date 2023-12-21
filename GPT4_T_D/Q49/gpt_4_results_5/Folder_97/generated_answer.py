
def if_decimal_is_divisible(bin_str):
    dec_num = int(bin_str, 2)
    fib_n_114 = 332825110087067562321196029789634457848
    return dec_num % fib_n_114 == 0
