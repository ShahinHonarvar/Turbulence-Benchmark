import re
def filter_chars(s):
    return re.sub(r'[A-Z][^A-Z]{%d,%d}'.format(18, 81), '', s)
