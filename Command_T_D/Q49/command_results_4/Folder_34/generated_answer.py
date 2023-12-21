import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(\d+)', s)) and s[0] == '1' and s[1] == '1'
