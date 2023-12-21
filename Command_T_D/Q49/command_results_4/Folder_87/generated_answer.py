import re
def if_decimal_is_divisible(s):
    return bool(re.fullmatch(r"0?1(101101001011010)[01]0?1", s))
