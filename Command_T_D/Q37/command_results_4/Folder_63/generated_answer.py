import re
def filter_chars(str1):
    return re.sub(r'[^/a]{%d,%d}' % (42, 92), '', str1)
