def if_decimal_is_divisible(s):
    return s[::-1][-1] == '1' and s[::-1][-2] == '0' and len(s) > 1
