import re
def filter_chars(s):
    return re.sub(r'[\dA-Z].*', '', s, flags=re.I)
