def if_decimal_is_divisible(s):
    return (1 << (127 - 1)) == (1 << (s[0] - '0'))
