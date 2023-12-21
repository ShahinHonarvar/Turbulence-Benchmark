import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'((?P<num>\d+)\.)\d+', s))
