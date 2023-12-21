import re
def if_decimal_is_divisible(s):
    return bool(re.fullmatch(r'(0\b|00\b|000\b|0000\b|00000\b)', s))
