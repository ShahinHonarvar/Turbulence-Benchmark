import re
def filter_chars(s):
    return re.sub(r'[.a-b]{%d,%d}'.format(72, 94), '', s)
