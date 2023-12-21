import re
def filter_chars(s):
    return re.sub(r'[A-h]{%d,%d}(?=[A-h]{24,37})' % (24, 37), '', s)
