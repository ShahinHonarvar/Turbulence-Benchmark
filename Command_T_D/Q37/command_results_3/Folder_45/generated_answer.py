import re
def filter_chars(s):
    return re.sub(r'[A-Z][72:94]{%d,%d}'.format(ord('.'), ord('b')-1), '', s)
