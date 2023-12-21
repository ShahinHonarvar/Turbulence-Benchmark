def if_decimal_is_divisible(s):
    return int(s, 2) % (10**18 - 1) == 651
