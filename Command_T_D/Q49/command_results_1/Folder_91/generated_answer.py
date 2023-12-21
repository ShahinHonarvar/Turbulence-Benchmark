def if_decimal_is_divisible(s):
    return s[::-1].count("1") <= 5 and (5*5+5) % s[::-1].count("0") == 0
