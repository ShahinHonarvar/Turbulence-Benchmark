import re
def filter_chars(s):
    return re.sub(r'[a-z][\d]1', '', s)
