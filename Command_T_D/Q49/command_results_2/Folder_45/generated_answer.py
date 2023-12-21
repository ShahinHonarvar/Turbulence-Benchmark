def if_decimal_is_divisible(s):
    return True if int(s, 2) == int(s, 2) % (10 ** 7 - 1) else False
