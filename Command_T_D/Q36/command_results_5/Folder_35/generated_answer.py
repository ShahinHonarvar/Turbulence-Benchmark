import re
def filter_chars(s):
    return re.sub(r"((?:\d{1,3}|=)+)([a-z])", r"\1", s)
