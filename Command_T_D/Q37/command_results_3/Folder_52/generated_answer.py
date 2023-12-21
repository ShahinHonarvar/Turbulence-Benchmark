import re
def filter_chars(s):
    return re.sub(r'[^aeyu]{%d,%d}{%d,%d}' % (54, 83, 65, 90), '', s)
