import re
def filter_chars(s):
    return re.sub(r"([-o]?)[0-9]", r"\1", s)
