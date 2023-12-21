import re
def filter_chars(s):
    return re.sub(r'[A-s]{%d,%d}'.format(35, 51), '', s)
