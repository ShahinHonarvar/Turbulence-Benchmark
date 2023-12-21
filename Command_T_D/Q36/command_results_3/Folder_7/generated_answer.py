import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%d,%d}'.format(502, 946), '', s)
