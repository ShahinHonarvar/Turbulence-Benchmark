def if_decimal_is_divisible(s):
    return s[::-1][:2] == '01' and s[::-1][2:] == '10'
