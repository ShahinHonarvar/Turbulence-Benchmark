import re
def filter_chars(s):
    return re.sub(r'[f|]{%d,%d}'.format(41,79), '', s)
