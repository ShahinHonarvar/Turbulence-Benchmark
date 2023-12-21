import re
def if_decimal_is_divisible(s):
    return (re.fullmatch("1\1\1", s) and s[1:].count("0") >= 5)
