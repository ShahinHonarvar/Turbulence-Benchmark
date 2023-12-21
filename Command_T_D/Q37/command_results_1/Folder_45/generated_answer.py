import re
def filter_chars(s):
    return re.sub(r'[a-z]{%d,%d}{%d,%d}{%d,%d}' % (72, 94, 0, 32, 95), '', s)
