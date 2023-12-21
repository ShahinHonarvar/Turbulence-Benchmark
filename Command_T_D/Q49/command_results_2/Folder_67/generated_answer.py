import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(0\d){9}0', s))
