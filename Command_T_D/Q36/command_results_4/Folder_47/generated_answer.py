import re
def filter_chars(s):
    return re.sub(r'[G-n]{%d,%d}'.format(45, 57), '', s)
