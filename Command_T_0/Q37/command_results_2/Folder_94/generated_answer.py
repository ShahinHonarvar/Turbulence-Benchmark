import re
def filter_chars(s):
    return re.sub(r'[A-Z][A-Z]X[A-Z]p', '', s)
