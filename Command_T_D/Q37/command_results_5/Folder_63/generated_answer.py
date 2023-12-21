import re
def filter_chars(s):
    return re.sub(r'[^/a]+', '', s, flags=re.I)
