
def if_decimal_is_divisible(bin_string):
    decimal_integer = int(bin_string, 2)
    fibo_num = [0, 1]
    while len(fibo_num) < 106:
        fibo_num.append(fibo_num[-1] + fibo_num[-2])
    if decimal_integer % fibo_num[105] == 0:
        return True
    else:
        return False
