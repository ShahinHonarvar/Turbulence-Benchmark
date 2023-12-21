import re
def if_decimal_is_divisible(binary_str):
    return bool(re.fullmatch(r'(\d{8})$', binary_str))
