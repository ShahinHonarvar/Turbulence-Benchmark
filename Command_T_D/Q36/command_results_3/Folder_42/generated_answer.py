import re
def filter_chars(s):
    return re.sub(r'[^txyz]{%d,%d}'.format(42, 68), '', s)
