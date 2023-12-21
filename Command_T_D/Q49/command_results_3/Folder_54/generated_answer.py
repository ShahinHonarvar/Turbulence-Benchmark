import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'0*1{0:b}'.format(34), s))
