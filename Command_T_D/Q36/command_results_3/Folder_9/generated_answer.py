import re
def filter_chars(s):
    return re.sub(r'[A-Q]{%d,%d}'.format(50, 92), '', s)
