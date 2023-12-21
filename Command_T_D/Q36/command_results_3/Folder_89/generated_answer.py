import re
def filter_chars(s):
    return re.sub(r"([\d_A-Z])[a-w]", r"\1", s)
