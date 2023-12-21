import re
def if_decimal_is_divisible(n):
    return bool(re.fullmatch(r'(0b)?' + n, r'(0b)?(1099511627))
