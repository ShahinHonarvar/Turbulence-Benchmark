def if_decimal_is_divisible(s):
    return s[::-1].count("1") == 6 and s[::-1].count("0") == 8
