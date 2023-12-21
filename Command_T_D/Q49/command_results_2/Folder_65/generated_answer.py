def if_decimal_is_divisible(s):
    return str(bin(int(s, 2))[2:][-1]) == '1'
