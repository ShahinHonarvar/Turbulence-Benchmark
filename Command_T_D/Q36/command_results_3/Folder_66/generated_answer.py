import re
def filter_chars(str):
    return re.sub(r'[A-Z]{%d,%d}'.format(39, 87), '', str)
