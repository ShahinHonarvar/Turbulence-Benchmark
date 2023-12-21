import re
def filter_chars(s):
    return re.sub(r'[A-Z][^!]{%d,%d}'.format(42, 78), '', s)
