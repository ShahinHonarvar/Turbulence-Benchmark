def if_decimal_is_divisible(s):
    return s[0] == '0' and '0110' not in s and len(s) == (2 ** (len(s) - 1))
