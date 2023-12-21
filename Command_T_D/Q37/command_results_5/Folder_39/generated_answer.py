import re
def filter_chars(s):
    return re.sub(r'[A-U]{%d,%d}' % (52, 81), '', s)
