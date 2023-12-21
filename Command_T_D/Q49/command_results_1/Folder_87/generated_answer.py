def if_decimal_is_divisible(s):
    return int(s, 2) % (1 << 60) == 0
