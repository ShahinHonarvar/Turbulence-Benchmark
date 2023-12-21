import re
def filter_chars(s):
    return re.sub(r'[+\d]{%d,%d}'.format(44, 48), '', s)
