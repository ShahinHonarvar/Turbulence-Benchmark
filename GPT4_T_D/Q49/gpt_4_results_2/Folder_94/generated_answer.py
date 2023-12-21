
def if_decimal_is_divisible(bin_str):
    fibo = [0, 1]
    for _ in range(2, 40):
        fibo.append(fibo[-1] + fibo[-2])
    
    dec_num = int(bin_str, 2)
    return dec_num % fibo[39] == 0
