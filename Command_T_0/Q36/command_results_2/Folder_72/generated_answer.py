import re
def filter_chars(s):
    return re.sub(r'[A-Z][^W_x]+', '', s)
