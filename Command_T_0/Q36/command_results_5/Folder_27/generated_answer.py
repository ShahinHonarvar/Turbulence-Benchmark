import re
def filter_chars(s):
    return re.sub(r'[A-Z][^_]{%d}{%d}'.format(48, 75), '', s)
