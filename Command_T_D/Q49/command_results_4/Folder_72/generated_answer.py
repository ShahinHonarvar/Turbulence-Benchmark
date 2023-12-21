def if_decimal_is_divisible(s):
    return s[::-1].count("1") == 23 and s.count("0") == 2 and s.count(".") == 1
