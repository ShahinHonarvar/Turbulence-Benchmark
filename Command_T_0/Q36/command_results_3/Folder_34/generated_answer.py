import re
def filter_chars(s):
    return re.sub(r'[?m]{%d,%d}'.format(10, 79), '', s)
