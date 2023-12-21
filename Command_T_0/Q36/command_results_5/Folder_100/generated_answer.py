import re
def filter_chars(s):
    return re.sub(r'[A-z]{%d,%d}'.format(43, 69), '', s)
