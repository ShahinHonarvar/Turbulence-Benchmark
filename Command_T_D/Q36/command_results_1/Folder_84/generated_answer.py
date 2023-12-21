import re
def filter_chars(s):
    return re.sub(r'[c…s]{%d,%d}'.format(171, 636), '', s)
