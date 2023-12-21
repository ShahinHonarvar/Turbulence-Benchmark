def if_decimal_is_divisible(s):
    return 1000000007 // 2 ** len(s) == int(s, 2)
