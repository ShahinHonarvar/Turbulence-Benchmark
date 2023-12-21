import re
def filter_chars(s):
    return re.sub(r'[a-z]{%d,%d}'.format(155, 403), '', s)
