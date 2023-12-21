import re
def filter_chars(s):
    return re.sub(r'[A-Z][a-z]', r' \1', s)
