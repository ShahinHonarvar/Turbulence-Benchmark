import re
def filter_chars(s):
    return re.sub(r'[P-x]', '', s, flags=re.I)
