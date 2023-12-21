def if_decimal_is_divisible(s):
    return s[::-1][-1] == '1' and (s[::-1][0] == '1' or s[::-1][1] == '1')
