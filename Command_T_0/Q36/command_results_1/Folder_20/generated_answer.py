import re
def filter_chars(s):
    return re.sub(r'[A-Z][^A-Z]{%d,%d}'.format(13,40), '', s)
