import re
def if_decimal_is_divisible(s):
    return bool(re.fullmatch(r'0b10*((?=00)01|10|11)', s))
