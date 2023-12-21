import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'0*1(?P<d>[01]+)0*1(?P<c>[01]+)', s))
