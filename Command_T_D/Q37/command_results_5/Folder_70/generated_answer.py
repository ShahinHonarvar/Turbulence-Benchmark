import re
def filter_chars(s):
    return re.sub(r'[+\-]{%d,%d}'.format(515, 538), '', s)
