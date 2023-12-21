import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%d,%d}'.format(18, 31), '', s)
