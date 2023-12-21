def if_decimal_is_divisible(s):
    i = s[::-1].index('1')
    return (i > 0) and (i < 4)
