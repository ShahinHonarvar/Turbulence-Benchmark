def if_decimal_is_divisible(s):
    return s[::-1][-1] == '1' and s[0] == '0' and s[1] == '1' and s[2] == '0'
