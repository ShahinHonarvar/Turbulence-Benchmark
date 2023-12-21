import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(1\d{1})\d{20}(0)', s))
