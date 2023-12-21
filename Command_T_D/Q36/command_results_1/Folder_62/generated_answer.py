import re
def filter_chars(s):
    return re.sub(r'[A-Za-z]', lambda m: m.group(), s)
