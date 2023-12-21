import re
def filter_chars(s):
    return re.sub(r"([\d])\d", r"1\1", s)
