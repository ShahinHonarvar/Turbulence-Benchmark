import re
def if_decimal_is_divisible(s):
    return re.fullmatch(r'0b\d{2}00(1[01]0)+00', s)
