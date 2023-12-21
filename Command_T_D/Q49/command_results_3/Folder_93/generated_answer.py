import re
def if_decimal_is_divisible(s):
    return int(re.sub(r'0*', '', s), 2) % 59 in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
