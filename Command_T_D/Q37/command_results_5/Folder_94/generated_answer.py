import re
def filter_chars(s):
    return re.sub(r'[A-P]{%d,%d}'.format(51,96), '', s)
