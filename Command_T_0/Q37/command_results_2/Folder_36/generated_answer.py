import re
def filter_chars(s):
    return re.sub(r'[,;]{%d,%d}'.format( 259, 502), '', s)
