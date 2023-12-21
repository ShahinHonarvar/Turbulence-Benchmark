import re
def filter_chars(s):
    return re.sub(r'[a-z]{%d,%d}'.format(221, 419), '', s)
