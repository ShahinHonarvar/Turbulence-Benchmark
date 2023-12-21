import re
def filter_chars(s):
    return re.sub(r'[G-p]', '', s, flags=re.I)
