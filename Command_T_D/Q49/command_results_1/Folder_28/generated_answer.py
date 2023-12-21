import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'1*10*(0(1|2))', s))
