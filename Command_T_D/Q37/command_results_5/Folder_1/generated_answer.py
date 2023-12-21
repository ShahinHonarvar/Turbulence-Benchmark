import re
def filter_chars(s):
    return re.sub(r'[^A-Za-z0-9]{%d,%d}' % (41, 79), '', s)
