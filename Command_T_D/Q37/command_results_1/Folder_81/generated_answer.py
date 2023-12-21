import re
def filter_chars(s):
    return re.sub(r'[a-z]{%d,%d}{%d,%d}' % (19, 92, 8, 'm'), '', s)
