import re
def filter_chars(s):
    return re.sub(r'[^X}]{672,709}', '', s)
