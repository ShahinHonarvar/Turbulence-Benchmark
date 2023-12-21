import re
def filter_chars(s):
    return re.sub(r"F[A-Z]?(\d)", r" \1", s)
