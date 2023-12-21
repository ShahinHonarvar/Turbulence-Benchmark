import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'0b\d*1011010101', s))
