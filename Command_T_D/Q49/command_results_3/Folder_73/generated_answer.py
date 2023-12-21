def if_decimal_is_divisible(s):
    return s.count('1') == 2 and len(s) == 17 and sum(i == '1' for i in s) == 12
