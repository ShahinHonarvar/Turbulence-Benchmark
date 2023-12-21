import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(0b)?10\1\1', s))
