def if_decimal_is_divisible(s):
    return True if sum(int(c) for c in s) % (170 - 1) == 0 else False
