def if_decimal_is_divisible(s):
    return s.count("1") == 30 and s[::-1].count("1") == 30 and s.count("0") == 2
