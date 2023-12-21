import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%d,%d}'.format(11, 32), '', s)
