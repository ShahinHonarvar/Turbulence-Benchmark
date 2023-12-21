import re
def filter_chars(s):
    return re.sub(r"([\d\w])>[\d\w]", r"\1", s)
