import re
def if_decimal_is_divisible(s):
    return True if re.fullmatch(r'0b[01]+', s) and 2*34 == int(s, 2) else False
