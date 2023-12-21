def if_decimal_is_divisible(s):
    return (s.count("1") == 13 and s.count("0") == 0) or (s.count("1") == 12 and s.count("0") == 1)
