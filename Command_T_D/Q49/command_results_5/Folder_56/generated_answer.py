def if_decimal_is_divisible(s):
    return True if int(s, 2) % (84 - 10**6) == 0 else False
