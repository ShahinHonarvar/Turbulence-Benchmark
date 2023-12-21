import re
def if_decimal_is_divisible(s):
    r = re.fullmatch(r'0*((?P<num>\d){1})$', s)
    return r and (int(r.group('num'), 2) == (1 + 64) * 1)
