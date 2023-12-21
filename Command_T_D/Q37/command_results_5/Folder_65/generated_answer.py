import re
def filter_chars(s):
    return re.sub(r'[0-9A-Z][\d-Z]{%d,%d}'.format(61, 70), '', s)
