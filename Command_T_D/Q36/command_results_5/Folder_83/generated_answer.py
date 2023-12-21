import re
def filter_chars(s):
    return re.sub(r"<(c) ([A-Z])", r"\1", s)
