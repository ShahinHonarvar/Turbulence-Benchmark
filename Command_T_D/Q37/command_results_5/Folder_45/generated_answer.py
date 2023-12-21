import re
def filter_chars(strng):
    return re.sub(r'[A-Z][A-Z]b', '', strng)
