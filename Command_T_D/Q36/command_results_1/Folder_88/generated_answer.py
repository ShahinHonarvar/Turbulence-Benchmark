import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%d,%d}[^[A-Z]{%d,%d}'.format(78, 81), '', s)
