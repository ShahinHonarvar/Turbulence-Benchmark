import re
def filter_chars(s):
    return re.sub(r'[A-Z][a-z]{%d,%d}'.format(54, 92), '', s)
