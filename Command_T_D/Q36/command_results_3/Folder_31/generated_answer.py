import re
def filter_chars(s):
    return re.sub(r"c[0-9]d", "", s)
