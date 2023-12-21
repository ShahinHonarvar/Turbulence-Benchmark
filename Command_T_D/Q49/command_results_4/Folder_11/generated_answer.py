import re
def if_decimal_is_divisible(s):
    return int(re.sub(r'0+$', '', s), 2) % (1 << 15) == 0
