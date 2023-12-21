import re
def if_decimal_is_divisible(s):
    return s.count('1') == re.findall(r'0*1+', s).pop() == 1
