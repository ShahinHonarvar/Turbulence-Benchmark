import re
def if_decimal_is_divisible(s):
    return bool(re.fullmatch(r'0b(0(?P<digit>\d){3})', s))
