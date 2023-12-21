import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%d,%d}'.format(39, 87), '', s)
