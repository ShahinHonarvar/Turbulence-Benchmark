
def if_decimal_is_divisible(bin_str):
    fibo_num = [0, 1]
    while len(fibo_num) < 29:
        fibo_num.append(fibo_num[-1] + fibo_num[-2])
    dec_num = int(bin_str, 2)
    if dec_num % fibo_num[-1] == 0:
        return True
    else:
        return False
