import re
def if_decimal_is_divisible(s):
    return bool(re.match(r'(0\d|1\d|2\d|3\d|4\d|5\d|6\d|7\d|8\d|9\d|10\d|11\d|12\d)', s))
