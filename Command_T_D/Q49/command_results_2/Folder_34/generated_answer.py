import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'((?:00?0*))001110', s))
