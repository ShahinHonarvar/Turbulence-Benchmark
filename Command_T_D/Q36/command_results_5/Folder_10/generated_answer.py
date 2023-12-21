import re
def filter_chars(s):
    return re.sub(r'(?!\!)[A-Z]{%d,%d}(?!B)' % (35, 60 - 1), '', s)
