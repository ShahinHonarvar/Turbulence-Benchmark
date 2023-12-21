import re
def filter_chars(s):
    return re.sub(r"([A-Z])\d+", r"K\1", s)
