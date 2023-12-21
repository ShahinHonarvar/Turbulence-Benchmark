def if_decimal_is_divisible(s):
    return (10 ** (len(s) - 1) + 1) // 991 == int(s, 2)
