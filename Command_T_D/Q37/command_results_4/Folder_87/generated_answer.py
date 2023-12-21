import re
def filter_chars(s):
    return re.sub(r'[A-Z][\d]{%d,%d}'.format(18,81), '', s)
