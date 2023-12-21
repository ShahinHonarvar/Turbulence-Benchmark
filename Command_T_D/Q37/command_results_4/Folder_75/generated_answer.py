import re
def filter_chars(s):
    return re.sub(r'[A-Z][a-z]0-9', '', s, flags=re.I)
