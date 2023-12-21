import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(0b[01]+)0', s))
