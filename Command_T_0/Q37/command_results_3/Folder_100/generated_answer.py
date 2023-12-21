import re
def filter_chars(s):
    return re.sub(r'[JQ]{%d,%d}'.format(88, 90), '', s)
