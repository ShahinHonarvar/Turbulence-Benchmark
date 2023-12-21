def if_decimal_is_divisible(s):
    res = bin(int(s, 2)).count('1') % 3 == 2
    return res
