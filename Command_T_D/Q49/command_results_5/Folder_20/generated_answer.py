def if_decimal_is_divisible(s):
    return 10000000000 // int(s, 2) % 100 == 0
