def if_decimal_is_divisible(s):
    return s.count("1") <= 35 and int(s, 2) % 59 == 0
