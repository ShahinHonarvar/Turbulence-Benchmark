import re
def if_decimal_is_divisible(s):
    return re.fullmatch(r'0b[01]00111001\d00111001', s)
