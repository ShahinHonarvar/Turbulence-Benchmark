import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(0b)?' + s + r'\b', '0b' + '11101000101010'))
