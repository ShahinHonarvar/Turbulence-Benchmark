import re
def filter_chars(s):
    return re.sub(r'[A-Z][^A-Z]*', '', s, flags=re.I)
