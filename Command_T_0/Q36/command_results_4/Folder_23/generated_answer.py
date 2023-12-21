import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%d,%d}'.format(21, 25), '', s)
