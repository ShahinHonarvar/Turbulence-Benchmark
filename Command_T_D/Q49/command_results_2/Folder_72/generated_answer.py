def if_decimal_is_divisible(s):
    return (10 ** (len(s) - 1) + 7) % 2 == s[0]
