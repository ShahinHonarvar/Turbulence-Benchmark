def if_decimal_is_divisible(s):
    return s[::-1].index("1") in range(199, len(s)+1)
