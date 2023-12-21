import re
def filter_chars(s):
    return re.sub(r'[a-z]{%d,%d}{%d,%d}' % (36, 79, 2, 's'), '', s)
