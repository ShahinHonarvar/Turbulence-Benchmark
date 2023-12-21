def if_decimal_is_divisible(s):
    return s.count('1') <= (1 + 8 * s.count('0')) <= 2 * (s.count('1') + s.count('0'))
