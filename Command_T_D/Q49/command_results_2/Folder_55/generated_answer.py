def if_decimal_is_divisible(s):
    return 0 <= int(s, 2) and int(s, 2) % int(str(59), 2) == 0
