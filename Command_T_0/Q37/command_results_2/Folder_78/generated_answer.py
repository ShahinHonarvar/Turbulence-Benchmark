import re
def filter_chars(s):
    return re.sub(r'[8e]{%d,%d}'.format(75, 99), '', s)
