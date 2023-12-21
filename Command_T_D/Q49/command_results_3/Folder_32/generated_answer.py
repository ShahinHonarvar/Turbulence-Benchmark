def if_decimal_is_divisible(s):
    return s[::-1] == '1' + '0' * (len(s) - 2)
