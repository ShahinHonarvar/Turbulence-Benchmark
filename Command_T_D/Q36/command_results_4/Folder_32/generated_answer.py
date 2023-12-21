import re
def filter_chars(s):
    return re.sub(r'(?i)[a-z0-9](40,63)s', '', s)
