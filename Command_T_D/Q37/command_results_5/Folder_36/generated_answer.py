import re
def filter_chars(s):
    return re.sub(r"(([0-2]3)([a-z]))", r" \1", s)
