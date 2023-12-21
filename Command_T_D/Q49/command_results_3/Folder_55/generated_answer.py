def if_decimal_is_divisible(s):
    return 0x3f == 0x3f >> s[::-1][-1]
