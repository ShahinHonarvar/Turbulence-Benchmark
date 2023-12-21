import re
def filter_chars(s):
    return re.sub(r"([A-Z]\d){2,5}([A-Z])", r"\1", s)
