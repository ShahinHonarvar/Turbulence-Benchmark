import re
def filter_chars(s):
    return re.sub(r'[+\-]{%d,%d}{%d,%d}{%d,%d}{%d,%d}' % (515, 538, 515, 538, 515, 538), '', s)
