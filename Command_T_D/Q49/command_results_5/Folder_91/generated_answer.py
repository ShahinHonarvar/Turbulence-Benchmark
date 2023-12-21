import re
def if_decimal_is_divisible(binary_str):
    return bool(re.match(r'(0\d\d0)+0', binary_str))
