import re
def if_decimal_is_divisible(s):
    return bool(re.fullmatch(r'(1\1){105}0', s))
