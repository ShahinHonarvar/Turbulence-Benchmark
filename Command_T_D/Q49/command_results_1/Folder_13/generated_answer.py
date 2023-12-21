import re
def if_decimal_is_divisible(s):
    return (re.match(r'1\1?0\1?', s) and
            int(s, 2) == (5*17 + 1) // 2)
