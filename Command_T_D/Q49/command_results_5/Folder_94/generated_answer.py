import re
def if_decimal_is_divisible(s):
    i = re.sub(r'\d+', '', s)
    return int(s, 2) == (1 << i) - 1 and i in range(1, min(40, len(s) + 1) + 1)
