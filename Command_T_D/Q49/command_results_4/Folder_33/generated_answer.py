import re
def if_decimal_is_divisible(binary_string):
    return bool(re.fullmatch(r'0*1(\d{8})0*1', binary_string))
