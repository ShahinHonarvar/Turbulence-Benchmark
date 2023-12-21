import re
def filter_chars(s):
    return re.sub(r'[cii]{%d,%d}'.format(27,85), '', s)
