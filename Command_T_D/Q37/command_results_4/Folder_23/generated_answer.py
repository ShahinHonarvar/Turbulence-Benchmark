import re
def filter_chars(s):
    return re.sub(r"<(V|v)+(Y|y)+>", "", s)
