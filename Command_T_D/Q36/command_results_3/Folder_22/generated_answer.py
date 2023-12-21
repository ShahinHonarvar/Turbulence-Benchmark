import re
def filter_chars(s):
    return re.sub(r'[a-z]', '', s, flags=re.I)
