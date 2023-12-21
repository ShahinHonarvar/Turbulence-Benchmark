import re
def filter_chars(s):
    return re.sub(r'[A-b]{%d,%d}'.format(35, 98), '', s)
