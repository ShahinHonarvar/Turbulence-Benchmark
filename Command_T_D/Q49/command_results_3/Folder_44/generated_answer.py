def if_decimal_is_divisible(s):
    return (1 << (len(s) - 1)) & s == (1 << (len(s) - 1))
