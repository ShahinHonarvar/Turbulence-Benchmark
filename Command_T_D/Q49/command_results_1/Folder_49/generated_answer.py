def if_decimal_is_divisible(s):
    return 100000000000**(len(s) - 1) % 95 == int(s, 2)
