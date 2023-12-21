import re
def filter_chars(s):
    return re.sub(r'<[A-Z]{%d,%d}>{%d,%d}'.format(26, 80, 26, 80), '', s)
