import re
def if_decimal_is_divisible(s):
    return re.fullmatch(r'0\1{13}(0+)', s)
