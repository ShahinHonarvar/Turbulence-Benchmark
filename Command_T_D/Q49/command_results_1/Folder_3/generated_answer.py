import re
def if_decimal_is_divisible(s):
    s = re.sub(r'0*', '', s)
    return s[0] == '1'
