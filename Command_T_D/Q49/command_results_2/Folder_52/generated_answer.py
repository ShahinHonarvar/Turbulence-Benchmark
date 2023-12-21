def if_decimal_is_divisible(s):
    return 1000000007 // 10**(len(s) - 1) == int(s, 2)
