import re
def filter_chars(s):
    return re.sub(r'[0-9][a-z]{%d,%d}'.format(32, 46), '', s)
