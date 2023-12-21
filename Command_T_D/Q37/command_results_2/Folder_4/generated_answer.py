import re
def filter_chars(s):
    return re.sub(r'[A-Z]{19,33}', '', s)
