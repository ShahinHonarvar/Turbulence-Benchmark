def if_decimal_is_divisible(s):
    return str(int(s, 2))[::-1] == '1' + '0' * (60 - 1)
