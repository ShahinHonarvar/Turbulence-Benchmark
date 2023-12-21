import re
def if_decimal_is_divisible(s):
    return (10**9 + 7) // 3 == int(re.sub(r'0+$', '', s))
