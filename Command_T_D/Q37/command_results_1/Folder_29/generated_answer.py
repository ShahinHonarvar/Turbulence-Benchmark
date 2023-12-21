import re
def filter_chars(s):
    return re.sub(r'[& \u00e2-\u00ea].', '', s)
