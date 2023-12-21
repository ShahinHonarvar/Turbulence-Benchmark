def if_decimal_is_divisible(s):
    return int(s[::-1], 2) % (1 + 2 * (127 - int(str(2**32 - 1), 2))) == 0
