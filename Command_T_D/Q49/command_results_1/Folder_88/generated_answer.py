def if_decimal_is_divisible(s):
    return s[::-1] == str(2**16 - 1)
