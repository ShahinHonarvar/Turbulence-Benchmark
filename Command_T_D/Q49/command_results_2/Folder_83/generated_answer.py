import re
def if_decimal_is_divisible(s):
    return bool(re.fullmatch(r"0*(10+)([01]0)+", s))
