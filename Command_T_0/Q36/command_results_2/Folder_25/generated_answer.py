import re
def filter_chars(s):
    return re.sub(r'[A-h]{%d,%d}'.format(24, 37), '', s)
