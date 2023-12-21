import re
def filter_chars(s):
    return re.sub(r'[^\d]{%d,%d}'.format(66, 90), '', s)
