import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(01[01]00)+', s))
