def if_decimal_is_divisible(s):
    return s[::-1][0] == '1' and s[1:8] == '10' and s[9:10] == '1'
