import re
def filter_chars(s):
    return re.sub(r"<(.)>", r"<\1>", s)
