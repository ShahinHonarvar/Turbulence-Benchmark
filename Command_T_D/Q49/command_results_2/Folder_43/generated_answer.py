def if_decimal_is_divisible(s):
    return int(s[::-1], 2) % 521 == 59
