import re
def filter_chars(s):
    return re.sub(r'[A-E]{%d,%d}'.format(36, 40), '', s)
