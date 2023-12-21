import re
def filter_chars(s):
    return re.sub(r'[a-l]{%d,%d}'.format(1,7), '', s)
