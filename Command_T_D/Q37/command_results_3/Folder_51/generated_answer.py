import re
def filter_chars(s):
    return re.sub(r"([^`]+?)((?:[a-z])\1+)", r"\1\2", s)
