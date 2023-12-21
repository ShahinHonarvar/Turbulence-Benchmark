import re
def filter_chars(s):
    return re.sub(r'[A-Z]{%d,%d}(=[A-Z]{%d,%d})[A-Z]{%d,%d}' % (35, 40, 35, 40, 35, 40), '', s)
