import re
def filter_chars(s):
    return re.sub(r'[;b]{%d,%d}'.format(27, 29), '', s)
